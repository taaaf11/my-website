from __future__ import annotations

import tomllib

from dataclasses import dataclass
from abc import ABC, abstractmethod


class SectionABC(ABC):
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

    @classmethod
    def from_data_file(cls, data_file_path: str) -> list[Link]:
        links = []

        try:
            with open(data_file_path) as f:
                links_data = tomllib.loads(f.read())
        except FileNotFoundError:
            return []

        for heading, data in links_data.items():
            links.append(
                cls(
                    **data,
                    heading=heading,
                )
            )

        return links

@dataclass
class MusicData:
    title: str
    album: str
    album_artwork_url: str
    artist: str
    spotify_url: str
    file_path: str | None

    @classmethod
    def from_data_file(cls, data_file_path: str = "music_data.toml") -> list[MusicData]:
        musics_data = []

        try:
            with open(data_file_path) as f:
                musics_data_data = tomllib.loads(f.read())
        except FileNotFoundError:
            return []

        for artist, songs in musics_data_data.items():
            for song in songs:
                # sets file_path key to None
                # when it is not present in data toml file
                song["file_path"] = song.get("file_path")

                music_data = cls(
                    **song,
                    artist=artist,
                )
                musics_data.append(music_data)

        return musics_data
