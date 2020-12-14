from dataclasses import dataclass, field
from typing import List


@dataclass
class Title:
    tconst: str
    schema: str = field(init=False, default="Title")


@dataclass
class Name:
    nconst: str
    schema: str = field(init=False, default="Name")


@dataclass
class Basics(Name):
    primary_name: str
    birth_year: int
    death_year: int
    primary_profession: List[str]
    known_for_titles: List[str]


@dataclass
class Akas(Title):
    ordering: int
    title: str
    region: str
    language: str
    types: List[str]
    attributes: List[str]
    is_original_title: bool


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


@dataclass
class Crew(Title):
    tconst: str
    directors: List[str]


@dataclass
class Episode(Title):
    writers: List[str]
