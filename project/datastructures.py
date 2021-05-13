from dataclasses import dataclass
from typing import List

@dataclass
class Site:
    '''
    This can represent things like buildings, restaurants, and parks.
    (e.g. Sears Tower, Chicago House of Blues, Millenium Park)
    '''
    name: str
    link: str
    total_posts: int
    lon: float
    lat: float

@dataclass
class Location:
    '''
    This can represent things like cities, neighborhoods, and bouroughs.
    (e.g. Chicago, Manhattan, Las Vegas)
    '''

    name: str
    link: str
    sites: List[Site]
