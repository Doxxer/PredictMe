#!/usr/bin/python

import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="root",
                     db="imdb")


def handle_actors(actors):
    ans = []
    ratings = db.cursor()
    for act in actors:
        params = act.split(" ")
        name = params[1] + ", " + params[0]
        ratings.execute("""select
        ratedActors.actor_rating
        from allNames
        inner join ratedActors on allNames.person_id = ratedActors.person_id
        where allNames.name = '{0}';""".format(name))
        res = ratings.fetchone()
        if res is not None:
            ans.append(res[0])
            if len(ans) == 5:
                return ans
    if len(ans) == 0:
        return [5.0]
    return ans


def handle_writers(actors):
    ans = []
    ratings = db.cursor()
    for act in actors:
        params = act.split(" ")
        name = params[1] + ", " + params[0]
        ratings.execute("""select
        ratedWriters.writer_rating
        from allNames
        inner join ratedWriters on allNames.person_id = ratedWriters.person_id
        where allNames.name = '{0}';""".format(name))
        res = ratings.fetchone()
        if res is not None:
            ans.append(res[0])
    if len(ans) == 0:
        return 5.0
    return sum(ans) / len(ans)


def handle_directors(actors):
    ans = []
    ratings = db.cursor()
    for act in actors:
        params = act.split(" ")
        name = params[1] + ", " + params[0]
        ratings.execute("""select
        ratedDirectors.director_rating
        from allNames
        inner join ratedDirectors on allNames.person_id = ratedDirectors.person_id
        where allNames.name = '{0}';""".format(name))
        res = ratings.fetchone()
        if res is not None:
            ans.append(res[0])
    if len(ans) == 0:
        return 5.0
    return sum(ans) / len(ans)


def get_rating(actors, directors, writers):
    ans = handle_actors(actors)
    length = len(ans)
    directors_rating = handle_directors(directors)
    writers_rating = handle_writers(writers)
    ans.append(directors_rating)
    ans.append(writers_rating)
    return tuple(ans), length


if __name__ == "__main__":
    print get_rating(["Keanu Reeves", "Rosamund Pike", "Neil Patrick Harris", "Ben Affleck"],
                     ["David Fincher"],
                     ["David Fincher"])