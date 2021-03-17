# PyMDB

This repo explores how Python dataclasses can described semi-structured data
(tsv files).
While this can be done using Pandas and SQLAlchemy, this repo is an excuse to
explore the (relatively) new Python dataclass object.

The goal is to take in IMDB provided
[TSV files](https://www.imdb.com/interfaces/)
and produce CSV files that can be ingested by Postgres.
A make file is included to create the Postgres database with the appropriate
tables and load the produced CSV files.
