DROP TABLE IF EXISTS title.akas;

CREATE TABLE title.akas (
  id SERIAL PRIMARY KEY,
  title_id text,
  ordering integer,
  title text,
  region text,
  language text,
  types text[],
  attributes text,
  is_original_title boolean
);

COPY title.akas(
  title_id,
  ordering,
  title,
  region,
  language,
  types,
  attributes,
  is_original_title)
FROM '/home/jlopez/git/imdb/csv/title.akas.csv' DELIMITER ',' CSV HEADER;
