# from typing import override
import time
from typing import Optional

import catppuccin
import flet as ft

from model import SectionABC, MusicData


class MusicControl(ft.Container):
    def __init__(self, music_data: MusicData, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.music_data = music_data
        self.content = ft.Row(
            [
                ft.Image(music_data.album_artwork_url, width=100, height=100),
                ft.Column(
                    [
                        ft.Text(
                            music_data.title,
                            font_family="Comfortaa",
                            weight=ft.FontWeight.BOLD,
                            size=18,
                        ),
                        ft.Text(
                            f"{music_data.artist} : : {music_data.album}",
                            font_family="Comfortaa",
                            weight=ft.FontWeight.W_300,
                            size=15,
                        ),
                    ]
                ),
            ]
        )
        self.ink = True
        self.tooltip = music_data.credits.strip()
        self.border = ft.border.all(1, catppuccin.PALETTE.frappe.colors.flamingo.hex)
        self.border_radius = 12
        self.padding = 15

        self.__audio: Optional[ft.Audio] = None

        self.on_click = lambda _: self.page.launch_url(music_data.spotify_url)
        self.on_hover = self._play_pause

    def did_mount(self) -> None:
        if self.music_data.file_path is not None:
            self.__audio = ft.Audio(self.music_data.file_path)
            self.page.overlay.append(self.__audio)
            self.page.update()

    def _play_pause(self, e) -> None:
        if self.__audio is None:
            return

        if e.data == "true":
            if self.__audio.volume != 1:
                self.__audio.volume = 1
                self.__audio.update()

            self.__audio.resume()

        else:
            # gradually decrease volume before pausing
            # while round(self.__audio.volume, 1) > 0:
            #     self.__audio.volume -= 0.1
            #     self.__audio.update()
            #
            #     time.sleep(0.1)

            self.__audio.pause()


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
