CREATE TABLE title.basics (
  tconst text UNIQUE PRIMARY KEY,
  title_type text,
  primary_title text,
  original_title text,
  is_adult boolean,
  start_year integer,
  end_year integer,
  runtime_minutes integer,
  genres text[]
);
