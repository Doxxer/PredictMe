#!/usr/bin/python
# coding=utf-8

import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="root",
                     # passwd="imdb",
                     db="imdb")


def fetch_person(person_name, database, fromTable_name):
    params = person_name.split(" ")
    name = params[1] + ", " + params[0]
    name = name.replace("'", "''")
    database.execute(u"""select
        {0}.actor_rating
        from Person
        inner join {0} on Person.person_id = {0}.person_id
        where Person.name = '{1}';""".format(fromTable_name, name))
    return database.fetchone()


def handle_actors(actors):
    result = []
    db_ratings = db.cursor()
    for act in actors:
        res = fetch_person(act, db_ratings, "ratedActors")
        if res:
            result.append(res[0])
            if len(result) == 5:
                return result
    if len(result) == 0:
        return [5.0]
    return result


def handle_actors_for_regression(actors):
    result = [0, 0, 0, 0]
    db_ratings = db.cursor()
    for act in actors:
        res = fetch_person(act, db_ratings, "ratedActors")
        if res:
            rating = res[0]
            if rating <= 2.5:
                result[0] += 1
            elif rating <= 5:
                result[1] += 1
            elif rating <= 7.5:
                result[2] += 1
            else:
                result[3] += 1
    return result


def handle_writers(actors):
    result = []
    db_ratings = db.cursor()
    for act in actors:
        res = fetch_person(act, db_ratings, "ratedWriters")
        if res:
            result.append(res[0])
    if len(result) == 0:
        return 5.0
    return sum(result) / len(result)


def handle_directors(actors):
    ans = []
    db_ratings = db.cursor()
    for act in actors:
        res = fetch_person(act, db_ratings, "ratedDirectors")
        if res:
            ans.append(res[0])
    if len(ans) == 0:
        return 5.0
    return sum(ans) / len(ans)


def get_rating(actors, directors, writers):
    ans = handle_actors(actors)
    length = len(ans)
    ans.append(handle_directors(directors))
    ans.append(handle_writers(writers))
    return tuple(ans), length


def get_rating_for_regression(actors, directors, writers):
    rating_tuple = handle_actors_for_regression(actors)
    rating_tuple.append(handle_directors(directors))
    rating_tuple.append(handle_writers(writers))

    return tuple(rating_tuple)


if __name__ == "__main__":
    print get_rating(["Keanu Reeves", "Rosamund Pike", "Neil Patrick Harris", "Ben Affleck"],
                     ["David Fincher"],
                     ["David Fincher"])
    print get_rating_for_regression(["Keanu Reeves", "Rosamund Pike", "Neil Patrick Harris", "Ben Affleck"],
                                    ["David Fincher"],
                                    ["David Fincher"])

    print get_rating([u"Timothée Chalamet"], [], [])
    print get_rating([u"Dean O'Gorman"], [], [])