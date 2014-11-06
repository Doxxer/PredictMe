#!/usr/bin/env python2

import MySQLdb
import pickle
from pybrain.datasets import SupervisedDataSet




db = MySQLdb.connect(host="localhost"
                     , user="root"
                     , passwd="@Q:27182;Byte"
                     , db="imdb2")

movies_cur = db.cursor()
movies_cur.execute("DROP TABLE IF EXISTS RatedDirectors;")
movies_cur.execute("DROP TABLE IF EXISTS RatedProducers;")

movies_cur.execute("""CREATE TABLE RatedDirectors AS
                    select person_id, movie_id, AVG(rating) as rating
                    from DirectorFULL
                    GROUP BY person_id;""")
movies_cur.execute("""CREATE TABLE RatedProducers AS
                    select person_id, movie_id, AVG(rating) as rating
                    from ProducerFULL
                    GROUP BY person_id;""")

actors_cur = db.cursor()
directors_cur = db.cursor()
producers_cur = db.cursor()


for actors_num in [1, 2, 3, 4, 5]:
    print actors_num

    dataset = SupervisedDataSet(3 + actors_num, 1)
    movies_cur.execute("DROP TABLE IF EXISTS RatedActors;")

    movies_cur.execute("""CREATE TABLE RatedActors AS
                        select person_id, movie_id, AVG(rating) as rating
                        from ActorsFULL
                        GROUP BY person_id
                        HAVING COUNT(person_id) >= {0};""".format(actors_num))

    movies_cur.execute("""select movie_id, rating, year from  allMovies
                        where movie_id in (
                          select movie_id from ActorsFULL
                          where person_id in (select person_id from RatedActors)
                        ) AND  movie_id in (
                          select movie_id from DirectorFULL
                        ) AND movie_id in (
                          select movie_id from ProducerFULL
                        )
                        ORDER BY RAND()
                        limit 100""")

    for movie in movies_cur:
        actors_cur.execute("""select rating from RatedActors
                              where person_id in (
                                 select person_id from ActorsFULL where movie_id = {0} )
                              ORDER BY rating desc limit {1}""".format(movie[0], actors_num))
        directors_cur.execute("""select rating from RatedDirectors
                              where person_id in (
                                 select person_id from DirectorFULL where movie_id = {0} )
                              ORDER BY rating desc limit 1""".format(movie[0]))
        producers_cur.execute("""select rating from RatedProducers
                              where person_id in (
                                 select person_id from ProducerFULL where movie_id = {0} )
                              ORDER BY rating desc limit 1""".format(movie[0]))

        actors_rates = tuple(actors_cur.fetchmany(actors_num)[0])
        # print actors_rates
        dataset.addSample((movie[2],) + actors_rates +
                          (producers_cur.fetchone()[0], directors_cur.fetchone()[0],), (movie[1],))

    with open('dataset_' + str(actors_num) + '.data', 'wb') as f:
        pickle.dump(dataset, f)

movies_cur.close()
actors_cur.close()
directors_cur.close()
producers_cur.close()
