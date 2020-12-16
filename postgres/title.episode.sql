DROP TABLE IF EXISTS title.episode;

CREATE TABLE title.episode(
  id SERIAL PRIMARY KEY,
  tconst text,
  parent_tconst text,
  season_number integer,
  episode_number integer
);

COPY title.episode(
  tconst,
  parent_tconst,
  season_number,
  episode_number)
FROM '/home/jlopez/git/imdb/csv/title.episode.csv'
WITH DELIMITER AS ',' QUOTE '"' ESCAPE '\' CSV HEADER;

CREATE UNIQUE INDEX ON title.episode (tconst);
