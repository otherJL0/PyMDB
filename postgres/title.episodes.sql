DROP TABLE IF EXISTS title.episodes;

CREATE TABLE title.episodes(
  id SERIAL PRIMARY KEY,
  tconst text,
  parent_tconst text,
  season_number integer,
  episode_number integer
);

COPY title.episodes(
  tconst,
  parent_tcont,
  season_number,
  episode_number)
FROM '/home/jlopez/git/imdb/data/csv/title.episodes.csv' CSV HEADER;
