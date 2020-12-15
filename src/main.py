from imdb_interfaces import *
from multiprocessing import Pool
import os

files = {}
files["name.basics.tsv"] = Name
files["title.akas.tsv"] = Akas
files["title.basics.tsv"] = Basics
files["title.crew.tsv"] = Crew
files["title.episode.tsv"] = Episode
files["title.principals.tsv"] = Principals
files["title.ratings.tsv"] = Ratings


def convert_to_csv(fname):
    outfile = open(f"csv/{fname.replace('tsv', 'csv')}", "w")
    with open(f"data/{fname}", "r") as tsv:
        for line in tsv:
            tmp = files[fname](*line.strip().split("\t"))
            outfile.write(str(tmp) + "\n")
        outfile.close()


if __name__ == "__main__":
    with Pool() as p:
        p.map(convert_to_csv, files.keys())
