#!/usr/bin/python
# coding=utf-8

import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="root",
                     # passwd="imdb",
                     db="imdb")


def fetch_person_rating_from_db(person_name, database, table_name):
    params = person_name.split(" ")
    name = params[1] + ", " + params[0]
    name = name.replace("'", "''")
    database.execute(u"""select
        {0}.actor_rating
        from Person
        inner join {0} on Person.person_id = {0}.person_id
        where Person.name = '{1}';""".format(table_name, name))
    return database.fetchone()


def get_average_rating(persons, table):
    result = []
    db_ratings = db.cursor()
    for p in persons:
        res = fetch_person_rating_from_db(p, db_ratings, table)
        if res:
            result.append(res[0])
    if len(result) == 0:
        return None
    return sum(result) / len(result)


def get_actor_rating(actors):
    result = []
    db_ratings = db.cursor()
    for act in actors:
        res = fetch_person_rating_from_db(act, db_ratings, "ratedActors")
        if res:
            result.append(res[0])
            if len(result) == 5:
                return result
    if len(result) == 0:
        return [5.0]
    return result


def get_avg_actor_rating(persons):
    return get_average_rating(persons, "ratedActors")


def get_writers_rating(persons):
    return get_average_rating(persons, "ratedWriters")


def get_directors_rating(persons):
    return get_average_rating(persons, "ratedDirectors")


def get_cast_rating_for_neurnets(actors, directors, writers):
    ans = get_actor_rating(actors)
    length = len(ans)
    ans.append(get_directors_rating(directors))
    ans.append(get_writers_rating(writers))
    return tuple(ans), length


def get_movie_info_for_regression(year, actors, directors, writers):
    a = get_avg_actor_rating(actors)
    d = get_directors_rating(directors)
    w = get_writers_rating(writers)
    return {
        "Year": year,
        "Actor": a if a else 5.0,
        "Director": d if d else 5.0,
        "Writer": w if w else 5.0,
    }


if __name__ == "__main__":
    print get_cast_rating_for_neurnets(["Keanu Reeves", "Rosamund Pike", "Neil Patrick Harris", "Ben Affleck"],
                                       ["David Fincher"],
                                       ["David Fincher"])
    print get_movie_info_for_regression(2014, ["Keanu Reeves", "Rosamund Pike", "Neil Patrick Harris", "Ben Affleck"],
                                       ["David Fincher"],
                                       ["David Fincher"])

    print get_cast_rating_for_neurnets([u"Timothée Chalamet"], [], [])
    print get_cast_rating_for_neurnets([u"Dean O'Gorman"], [], [])