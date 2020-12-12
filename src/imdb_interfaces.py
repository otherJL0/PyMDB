from dataclasses import dataclass
from typing import List


@dataclass
class name_basics:
    """ Class to keep track of peoples' names """

    nconst: str  # Unique alphanumeric ID
    primary_name: str
    birth_year: int
    death_year: int
    primary_profession: List[str]
    known_for_titles: List[str]
