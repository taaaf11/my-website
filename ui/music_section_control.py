# from typing import override
from typing import Optional

import catppuccin
import flet as ft

from model import SectionABC, MusicData


class MusicControl(ft.Container):
    def __init__(self, music_data: MusicData, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.music_data = music_data
        self.playing_note_icon = ft.Container(
            ft.Icon(
                ft.Icons.MUSIC_NOTE_ROUNDED,
                size=27,
                color=catppuccin.PALETTE.frappe.colors.lavender.hex,
            ),
            margin=ft.margin.Margin(left=0, top=0, right=10, bottom=0),
            opacity=0,
            animate_opacity=ft.animation.Animation(duration=150),
        )

        self.content = ft.Row(
            [
                ft.Row(
                    [
                        ft.Image(music_data.album_artwork_url, width=100, height=100),
                        ft.Column(
                            [
                                ft.Text(
                                    music_data.title,
                                    font_family="Comfortaa",
                                    weight=ft.FontWeight.W_600,
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
                ),
                self.playing_note_icon,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
            # show note icon
            self.playing_note_icon.opacity = 1
            self.playing_note_icon.update()

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

            # hide note icon
            self.playing_note_icon.opacity = 0
            self.playing_note_icon.update()

            self.__audio.pause()


class MusicSectionControl(ft.Container, SectionABC):
    def __init__(self, musics_data: list[MusicData]):
        super().__init__()

        self.musics_data = musics_data
        self.content = ft.Column(
            [
                ft.Text("My favorite music (hover to play).", size=16),
            ]
                +
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
    def is_empty(self) -> bool:
        return not bool(self.musics_data)
