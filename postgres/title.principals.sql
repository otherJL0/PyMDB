DROP TABLE IF EXISTS title.principals;

CREATE TABLE title.principals(
  id SERIAL PRIMARY KEY,
  tconst text,
  ordering integer,
  nconst text,
  categery text,
  job text,
  characters text
);

COPY title.principals(
  tconst,
  ordering,
  nconst,
  category,
  job,
  characters)
FROM '/home/jlopez/git/imdb/csv/title.principals.csv' CSV HEADER;
