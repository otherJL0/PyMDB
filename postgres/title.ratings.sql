DROP TABLE IF EXISTS title.ratings;

CREATE TABLE title.ratings(
  id SERIAL PRIMARY KEY,
  tconst text,
  average_rating real,
  num_votes integer
);

COPY title.ratings(
  tconst,
  average_rating,
  num_votes)
FROM '/home/jlopez/git/imdb/csv/title.ratings.csv' CSV HEADER;
