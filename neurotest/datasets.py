#!/usr/bin/env python2

import MySQLdb
import pickle


db = MySQLdb.connect(host="localhost"
                     , user="imdb2"
                     , passwd="imdb2"
                     , db="imdb2")
movies_cur = db.cursor()

movies_cur.execute("DROP TABLE IF EXISTS RatedActors;")
movies_cur.execute("DROP TABLE IF EXISTS RatedDirectors;")
movies_cur.execute("DROP TABLE IF EXISTS RatedProducers;")

movies_cur.execute("""CREATE TABLE RatedActors AS
                    select person_id, movie_id, AVG(rating) as rating
                    from ActorsFULL
                    GROUP BY person_id;""")
movies_cur.execute("""CREATE TABLE RatedDirectors AS
                    select person_id, movie_id, AVG(rating) as rating
                    from DirectorFULL
                    GROUP BY person_id;""")
movies_cur.execute("""CREATE TABLE RatedProducers AS
                    select person_id, movie_id, AVG(rating) as rating
                    from ProducerFULL
                    GROUP BY person_id;""")

datasets = []
for i in range(6):
    print i
    datasets.append([])
    movies_cur.execute("""select movie_id, rating, year from  allMovies
                        where movie_id in (
                          select movie_id from ActorsFULL
                        ) AND  movie_id in (
                          select movie_id from DirectorFULL
                        ) AND movie_id in (
                          select movie_id from ProducerFULL
                        )
                        ORDER BY RAND()
                        limit 100""")

    actors_cur = db.cursor()
    directors_cur = db.cursor()
    producers_cur = db.cursor()
    for movie in movies_cur:
        actors_cur.execute("""select rating from RatedActors
                              where person_id in (
                                 select person_id from ActorsFULL where movie_id = {0} )
                              ORDER BY rating desc limit 1""".format(movie[0]))
        directors_cur.execute("""select rating from RatedDirectors
                              where person_id in (
                                 select person_id from DirectorFULL where movie_id = {0} )
                              ORDER BY rating desc limit 1""".format(movie[0]))
        producers_cur.execute("""select rating from RatedProducers
                              where person_id in (
                                 select person_id from ProducerFULL where movie_id = {0} )
                              ORDER BY rating desc limit 1""".format(movie[0]))
        datasets[i].append([(movie[2], actors_cur.fetchone()[0], directors_cur.fetchone()[0], producers_cur.fetchone()[0],), (movie[1],)])

movies_cur.close()
actors_cur.close()
directors_cur.close()
producers_cur.close()

with open('datasets.pickle', 'wb') as f:
    pickle.dump(datasets, f)