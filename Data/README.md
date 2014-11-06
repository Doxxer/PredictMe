
Только база данных для фильмов !!! 

0) allMovies (movie_id, рейтинг, бюджет, год) movie_id будет таким же как если вы сделаете запрос через интернет к файлу, взят с их базы
movie_id(Primary key)	rating		budge		year
1) ActorsFull (id, id актера, id фильма, рейтинг фильма, бюджет, год выхода)
a(Primary key)		person_id(Key)		movie_id		rating		budge		year
2) ActorsShort (id, id актера, id фильма) // можно подцепиться к файлу allMovies и добавить остальные параметры 
a(Primary key)		person_id(Key)		movie_id

3)4)5) в аналогичном формате пары таблиц Producer, Director, Writer

6) allNames(person_id, name) - имя человека

