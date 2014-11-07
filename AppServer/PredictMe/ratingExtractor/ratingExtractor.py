#!/usr/bin/python

import MySQLdb
import pickle

db = MySQLdb.connect(host="localhost"
                     , user="root"
                     , db="imdb")
                     
def handleActors(actors):
	ans = []
	ratings = db.cursor()
	for act in actors:
		params = act.split(" ")
		name = params[1] + ", " + params[0]
		ratings.execute("""select
		  ratedActors.actor_rating
		from allNames
		  inner join ratedActors on allNames.person_id = ratedActors.person_id 
		where allNames.name = %s;""", (name))		
		res =	ratings.fetchone()
		if res is not None:
			ans.append(res[0])
			if len(ans)==5:
				return ans
	if len(ans) == 0:
		return [5.0]
	return ans


def handleWriters(actors):
	ans = []
	ratings = db.cursor()
	for act in actors:
		params = act.split(" ")
		name = params[1] + ", " + params[0]
		ratings.execute("""select
		  ratedWriters.writer_rating
		from allNames
		  inner join ratedWriters on allNames.person_id = ratedWriters.person_id 
		where allNames.name = %s;""", (name))		
		res =	ratings.fetchone()
		if res is not None:
			ans.append(res[0])
	if len(ans) == 0:
		return 5.0
	return sum(ans)/len(ans)



def handleDirectors(actors):
	ans = []
	ratings = db.cursor()
	for act in actors:
		params = act.split(" ")
		name = params[1] + ", " + params[0]
		ratings.execute("""select
		  ratedDirectors.director_rating
		from allNames
		  inner join ratedDirectors on allNames.person_id = ratedDirectors.person_id 
		where allNames.name = %s;""", (name))		
		res =	ratings.fetchone()
		if res is not None:
			ans.append(res[0])
	if len(ans) == 0:
		return 5.0
	return sum(ans)/len(ans)


def ratingsExtractor(actors, directors, writers):			
	ans = handleActors(actors)
	length = len(ans) 
	directorsRating = handleDirectors(directors)
	writersRating = handleWriters(writers)
	ans.append(directorsRating)
	ans.append(writersRating)
	return (ans, length)

if __name__ == "__main__":
    actors = ["Keanu Reeves",  "Rosamund Pike", "Neil Patrick Harris", "Ben Affleck"]
    directors = ["David Fincher"]
    writers = ["David Fincher"]
    print ratingsExtractor(actors, directors, writers)
	


