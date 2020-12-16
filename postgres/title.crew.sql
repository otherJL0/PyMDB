DROP TABLE IF EXISTS title.crew;

CREATE TABLE title.crew(
  id SERIAL PRIMARY KEY,
  tconst text,
  directors text[],
  writers text[]
);

COPY title.crew(
  tconst,
  directory,
  writers)
FROM '/home/jlopez/git/imdb/csv/title.crew.csv' CSV HEADER;
