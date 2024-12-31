from __future__ import annotations

import string
import tomllib

from dataclasses import dataclass
from abc import ABC, abstractmethod
from random import choice

import catppuccin
from catppuccin.models import Color


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
class ContactData:
    icon_char: str
    heading: str
    username: str
    url: str
    card_color: str

    # static class attribute
    # used when using random colors
    # for each card
    # colors in this card would not
    # be used for next random color
    used_card_colors = []

    def __post_init__(self):
        for color in catppuccin.PALETTE.frappe.colors:
            if color.name.rstrip(string.digits) in {
                "text", "subtext", "overlay", "surface", "base", "mantle", "crust"
            }:
                if color not in ContactData.used_card_colors:
                    ContactData.used_card_colors.append(color)

    @staticmethod
    def _generate_random_color() -> Color:
        ctp_colors = list(catppuccin.PALETTE.frappe.colors)

        while (card_color := choice(ctp_colors)) in ContactData.used_card_colors:
            continue

        return card_color

    @classmethod
    def from_data_file(cls, data_file_path: str = "contact_data.toml") -> list[ContactData]:
        contact_datas = []

        try:
            with open(data_file_path, encoding="utf-8") as f:
                contact_datas_data = tomllib.loads(f.read())
        except FileNotFoundError:
            return []

        for heading, data in contact_datas_data.items():
            contact_datas.append(
                cls(
                    **data,
                    heading=heading,
                    card_color=ContactData._generate_random_color().hex,
                )
            )

        return contact_datas


@dataclass
class MusicData:
    title: str
    album: str
    album_artwork_url: str
    artist: str
    spotify_url: str
    file_path: str | None
    credits: str

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
