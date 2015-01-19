insert into ratedDirectors
SELECT p.person_id, avg(p.rating), 0 as train
FROM PersonsFULL p
  INNER JOIN
  (SELECT m.title_id
   FROM Movies m
   WHERE m.votes % 10 in (0, 1, 2)
   GROUP BY m.title_id
  ) movr ON (p.title_id = movr.title_id)
WHERE p.role_id IN (8)
GROUP BY p.person_id;


SELECT a.person_id, abs(max(actor_rating)-min(actor_rating))
from ratedActors a
GROUP BY a.person_id
HAVING count(a.person_id) = 2 and abs(max(actor_rating)-min(actor_rating)) > 2
ORDER BY 2 desc;

delete FROM ratedActors;