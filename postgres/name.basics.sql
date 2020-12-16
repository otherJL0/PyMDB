DROP TABLE IF EXISTS name.basics;

CREATE TABLE name.basics(
  id SERIAL PRIMARY KEY,
  nconst text,
  primary_name text,
  birth_year integer,
  death_year integer,
  primary_profession text[],
  known_for_titles text[]
);

COPY name.basics(
  nconst,
  primary_name,
  birth_year,
  death_year,
  primary_profession,
  known_for_titles)
FROM '/home/jlopez/git/imdb/csv/name.basics.csv'
WITH DELIMITER AS ',' QUOTE '"' ESCAPE '\' CSV HEADER;

CREATE UNIQUE INDEX ON name.basics (nconst);
