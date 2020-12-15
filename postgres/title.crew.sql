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
FROM 'csv/title.crew.csv' DELIMITER ',' CSV HEADER;
