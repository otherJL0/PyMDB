CREATE TABLE title.akas (
  tconst text UNIQUE PRIMARY KEY,
  ordering integer,
  title text,
  region text,
  language text,
  types text[],
  attributes text,
  is_original_title boolean
);
