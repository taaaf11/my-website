# from typing import override

import catppuccin
import flet as ft

from model import SectionABC, MusicData


class MusicControl(ft.Container):
    # def __init__(self, title: str, album: str, album_artwork_url: str, artist: str, spotify_url: str, *args, **kwargs):
    def __init__(self, music_data: MusicData, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.content = ft.Row(
            [
                ft.Image(music_data.album_artwork_url, width=100, height=100),
                ft.Column(
                    [
                        ft.Text(music_data.title, font_family="Comfortaa", weight=ft.FontWeight.BOLD, size=18),
                        ft.Text(f"{music_data.artist} : : {music_data.album}", font_family="Comfortaa", weight=ft.FontWeight.W_300, size=15)
                    ]
                )
            ]
        )
        self.ink = True
        self.border = ft.border.all(
            1,
            catppuccin.PALETTE.frappe.colors.flamingo.hex
        )
        self.border_radius = 12
        self.padding = 15

        self.on_click = lambda _: self.page.launch_url(music_data.spotify_url)


class MusicSectionControl(ft.Container, SectionABC):
    def __init__(self, musics_data: list[MusicData]):
        super().__init__()

        self.musics_data = musics_data
        self.content = ft.Column(
            [
                MusicControl(music_data, margin=ft.margin.symmetric(vertical=5))
                for music_data in musics_data
            ]
        )

    # @override
    @property
    def section_header(self) -> str:
        return "Music"

    # @override
    @property
    def is_empty(self):
        return not bool(self.musics_data)
