DB=imdb
BUILD=${CURDIR}/imdb.sql
SCRIPTS=${CURDIR}/postgres
CSV='${CURDIR}/csv'

all: title.akas
	echo "All tables have been built"


title.akas: title.basics
	psql $(DB) -f $(SCRIPTS)/title.akas.sql

title.basics: title.crew
	psql $(DB) -f $(SCRIPTS)/title.basics.sql

title.crew: title.episode
	psql $(DB) -f $(SCRIPTS)/title.crew.sql

title.episode: title.ratings
	psql $(DB) -f $(SCRIPTS)/title.episode.sql

title.principals:
	psql $(DB) -f $(SCRIPTS)/title.principals.sql

title.ratings: name.basics
	psql $(DB) -f $(SCRIPTS)/title.ratings.sql

name.basics:
	psql $(DB) -f $(SCRIPTS)/name.basics.sql
