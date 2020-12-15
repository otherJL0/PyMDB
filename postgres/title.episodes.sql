CREATE TABLE title.episodes(
  tconst text UNIQUE PRIMARY KEY,
  parent_tconst text,
  season_number integer,
  episode_number integer
);
