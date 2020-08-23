import requests
from datetime import datetime
from datetime import timedelta

table_names = ["name.basics", "title.akas", "title.basics",
               "title.crew", "title.episodes", "title.principals", "title.ratings"]
url = "https://datasets.imdbws.com/{}.tsv.gz"

data = []
total_download_time = 0.0
for dataset in [url.format(table) for table in table_names]:
    print(dataset.split("/")[-1])
    download_start_time = datetime.now()
    data.append(requests.get(dataset))
    time_to_download: timedelta = datetime.now() - download_start_time
    print(
        f"{len(data[-1].content)} downloaded in time to download: {time_to_download.total_seconds()}")
    total_download_time += time_to_download.total_seconds()
