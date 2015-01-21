CREATE TABLE Rating
(
  ID         INT,
  Title      LONGTEXT NOT NULL,
  Year       INT,
  Budget     DOUBLE   NOT NULL,
  Actor      REAL,
  Director   REAL,
  Writer     REAL,
  Popularity INT
);

INSERT INTO Rating
  SELECT
    m.title_id            AS 'ID',
    m.title               AS 'Title',
    m.production_year     AS 'Year',
    m.budget              AS 'Budget',
    avg(act.actor_rating) AS 'Actor',
    avg(dir.actor_rating) AS 'Director',
    avg(wr.actor_rating)  AS 'Writer',
    m.popularity          AS 'Popularity'
  FROM (
         SELECT DISTINCT
           m1.title_id,
           m1.title,
           m1.production_year,
           m1.budget,
           m1.votes,
           m1.popularity
         FROM Movies m1
       ) m
    INNER JOIN PersonsFULL p ON (p.title_id = m.title_id)
    LEFT JOIN ratedActors act ON (p.person_id = act.person_id AND p.role_id IN (1, 2))
    LEFT JOIN ratedDirectors dir ON (p.person_id = dir.person_id AND p.role_id = 8)
    LEFT JOIN ratedWriters wr ON (p.person_id = wr.person_id AND p.role_id = 4)
  GROUP BY m.title_id;