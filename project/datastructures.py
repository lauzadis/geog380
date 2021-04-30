from dataclasses import dataclass
from typing import List

@dataclass
class Site:
    name: str
    link: str
    total_posts: int
    lon: float
    lat: float

@dataclass
class Location:
    name: str
    link: str
    sites: List[Site]
