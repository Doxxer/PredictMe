SELECT
  m.title_id                 AS 'Film',
  m.rating                   AS 'Rating',
  m.production_year          AS 'Year',
  m.budget                   AS 'Budget',
  sum(act.actor_rating < 6)  AS 'Actor.Group1',
  sum(act.actor_rating >= 6) AS 'Actor.Group2',
  avg(dir.actor_rating)      AS 'Director',
  avg(wr.actor_rating)       AS 'Writer',
  m.popularity               AS 'Popularity'
FROM (
       SELECT DISTINCT
         m1.title_id,
         m1.rating,
         m1.production_year,
         m1.budget,
         m1.votes,
         m1.popularity
       FROM Movies m1
     ) m
  INNER JOIN PersonsFULL p ON (p.title_id = m.title_id)
  LEFT JOIN ratedActors act ON (p.person_id = act.person_id AND act.train = 1 AND p.role_id IN (1, 2))
  LEFT JOIN ratedDirectors dir ON (p.person_id = dir.person_id AND dir.train = 1 AND p.role_id = 8)
  LEFT JOIN ratedWriters wr ON (p.person_id = wr.person_id AND wr.train = 1 AND p.role_id = 4)
WHERE
  votes % 10 NOT IN (0, 1, 2)
-- AND m.title_id = 2908369;
GROUP BY m.title_id;