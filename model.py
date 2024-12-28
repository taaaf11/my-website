from dataclasses import dataclass
# from typing import Protocol
from abc import ABC, abstractmethod


# nothing to do with `Animatable` in other languages
class AnimatableSectionABC(ABC):
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @property
    @abstractmethod
    def section_header(self) -> str:
        ...


# a link in link-tree
@dataclass
class Link:
    heading: str | None
    description: str
    url: str

    def __post_init__(self):
        if self.heading is None:
            self.heading = self.url

@dataclass
class MusicData:
    title: str
    album: str
    album_artwork_url: str
    artist: str
    spotify_url: str
