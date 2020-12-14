CREATE TABLE name.basics(
  nconst text UNIQUE PRIMARY KEY,
  primary_name text,
  birth_year integer,
  death_year integer,
  primary_profession text[],
  known_for_titles text[]
);
