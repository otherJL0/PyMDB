from dataclasses import dataclass, field
from typing import List


def list_join(l):
    result = ",".join(l)
    return "{" + result + "}"


class Schema:
    def __init__(self, schema_name):
        self.schema = schema_name
        self.result = []

    def __repr__(self):
        return "\t".join(result)


@dataclass
class Name(Schema):
    schema = "name"


@dataclass
class Title(Schema):
    schema = "title"


@dataclass
class Basics(Name):
    nconst: str
    primary_name: str
    birth_year: int
    death_year: int
    primary_profession: List[str]
    known_for_titles: List[str]

    def __post_init__(self):
        self.result.append(self.nconst)
        self.result.append(self.primary_name)
        self.result.append(self.birth_year)
        self.result.append(self.death_year)
        self.result.append(list_join(self.primary_profession))
        self.result.append(list_join(self.known_for_titles))


@dataclass
class Akas(Title):
    title_id: str
    ordering: int
    title: str
    region: str
    language: str
    types: List[str]
    attributes: List[str]
    is_original_title: bool

    def __post_init__(self):
        self.result.append(self.ordering)
        self.result.append(self.title)
        self.result.append(self.region)
        self.result.append(self.language)
        self.result.append(list_join(self.types))
        self.result.append(list_join(self.attributes))
        self.result.append(self.is_original_title)


@dataclass
class Basics(Title):
    tconst: str
    title_type: str
    primary_title: str
    original_title: str
    is_adult: bool
    start_year: int
    end_year: int
    runtime_minutes: int
    genres: List[str]

    def __post_init__(self):
        result = []
        self.result.append(self.tconst)
        self.result.append(self.title_type)
        self.result.append(self.primary_title)
        self.result.append(self.original_title)
        self.result.append(self.is_adult)
        self.result.append(self.start_year)
        self.result.append(self.end_year)
        self.result.append(self.runtime_minutes)
        self.result.append(list_join(self.genres))
        return "\t".join(result)


@dataclass
class Principals(Title):
    tconst: str
    ordering: int
    nconst: str
    category: str
    job: str
    characters: str

    def __post_init__(self):
        self.result.append()


@dataclass
class Crew(Title):
    tconst: str
    directors: List[str]

    def __post_init__(self):
        self.result.append(self.tconst)
        self.result.append(list_join(self.directors))


@dataclass
class Episode(Title):
    tconst: str
    parent_tconst: str
    season_number: int
    episode_number: int

    def __post_init__(self):
        self.result.append(self.tconst)
        self.result.append(self.parent_tconst)
        self.result.append(self.season_number)
        self.result.append(self.episode_number)


@dataclass
class Ratings(Title):
    tconst: str
    average_rating: float
    num_votes: int

    def __post_init__(self):
        self.result.append(self.tconst)
        self.result.append(self.average_rating)
        self.result.append(self.num_votes)
