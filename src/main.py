from multiprocessing import Pool

import imdb_interfaces as imdb

FILE_INTERFACE_MAPPINGS = {
    "name.basics.tsv": imdb.Name,
    "title.akas.tsv": imdb.Akas,
    "title.basics.tsv": imdb.Basics,
    "title.crew.tsv": imdb.Crew,
    "title.episode.tsv": imdb.Episode,
    "title.principals.tsv": imdb.Principals,
    "title.ratings.tsv": imdb.Ratings,
}


def convert_to_csv(tsv_infile: str):
    """ Converts a TSV file into a CSV file to be read by Postgres """
    csv_outfile = open(f"csv/{tsv_infile.replace('tsv', 'csv')}", "w")
    with open(f"data/{tsv_infile}", "r") as tsv:
        for tsv_line in tsv:
            tmp = FILE_INTERFACE_MAPPINGS[tsv_infile](*tsv_line.strip().split("\t"))
            csv_outfile.write(str(tmp) + "\n")
        csv_outfile.close()


if __name__ == "__main__":
    with Pool() as p:
        """ Converts each file in parallel """
        p.map(convert_to_csv, FILE_INTERFACE_MAPPINGS.keys())
