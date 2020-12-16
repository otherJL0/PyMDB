DROP TABLE IF EXISTS title.crew;

CREATE TABLE title.crew(
  id SERIAL PRIMARY KEY,
  tconst text,
  directors text[],
  writers text[]
);

COPY title.crew(
  tconst,
  directors,
  writers)
FROM '/home/jlopez/git/imdb/csv/title.crew.csv'
WITH DELIMITER AS ',' QUOTE '"' ESCAPE '\' CSV HEADER;

CREATE UNIQUE INDEX ON title.crew (tconst);
