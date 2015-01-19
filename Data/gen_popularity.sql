SELECT
  m.gener,
  Genre.gener,
  count(m.id)
FROM Movies m
  INNER JOIN Genre ON (Genre.id = m.gener)
GROUP BY m.gener
-- HAVING count(m.id) > 700
ORDER BY 3 DESC;

UPDATE Movies
SET popularity = 1;
UPDATE Movies m1, (SELECT DISTINCT m.title_id
                   FROM Movies m
                   WHERE m.gener NOT IN (1, 3, 6, 8, 10, 13, 14, 18, 22, 25, 26, 30)) m2
SET popularity = 0
WHERE m1.title_id = m2.title_id;

SELECT count(DISTINCT m.title_id)
FROM Movies m
WHERE m.popularity = 0;