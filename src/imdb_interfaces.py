from dataclasses import dataclass, field
from typing import List


@dataclass
class Title:
    tconst: str
    schema: str = field(init=False, default="title")


@dataclass
class Name:
    nconst: str
    schema: str = field(init=False, default="name")


@dataclass
class Basics(Name):
    primary_name: str
    birth_year: int
    death_year: int
    primary_profession: List[str]
    known_for_titles: List[str]

    def __post_init_(self):
        self.birth_year = int(self.birth_year)
        self.death_year = int(self.death_year)


@dataclass
class Akas(Title):
    ordering: int
    title: str
    region: str
    language: str
    types: List[str]
    attributes: List[str]
    is_original_title: bool

    def __post_init(self):
        self.ordering = int(self.ordering)
        self.is_original_title = bool(self.is_original_title)


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
        self.is_adult = bool(self.is_adult)
        self.start_year = int(self.start_year)
        self.end_year = int(self.end_year)
        self.runtime_minutes = int(self.runtime_minutes)


@dataclass
class Crew(Title):
    tconst: str
    directors: List[str]


@dataclass
class Episode(Title):
    writers: List[str]
