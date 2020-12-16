DROP TABLE IF EXISTS title.basics;

CREATE TABLE title.basics (
  id SERIAL PRIMARY KEY,
  tconst text,
  title_type text,
  primary_title text,
  original_title text,
  is_adult boolean,
  start_year integer,
  end_year integer,
  runtime_minutes integer,
  genres text[]
);

COPY title.basics(
  tconst,
  title_type,
  primary_title,
  original_title,
  is_adult,
  start_year,
  end_year,
  runtime_minutes,
  genres)
FROM '/home/jlopez/git/imdb/csv/title.basics.csv' CSV HEADER;
