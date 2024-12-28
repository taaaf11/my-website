from __future__ import annotations

import tomllib

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

    @classmethod
    def from_data_file(cls, data_file_path: str = "music_data.toml") -> list[MusicData]:
        musics_data = []
        with open(data_file_path) as f:
            musics_data_data = tomllib.loads(f.read())

        for artist, songs in musics_data_data.items():
            for song in songs:
                music_data = cls(
                    **song,
                    artist=artist,
                )
                musics_data.append(music_data)

        return musics_data
