# from typing import override

import catppuccin
import flet as ft

from model import AnimatableSectionABC


class NothingToShowControl(ft.Container, AnimatableSectionABC):
    def __init__(self):
        super().__init__()
        cat_text = ft.Text(
            "/⁠ᐠ⁠｡⁠ꞈ⁠｡⁠ᐟ⁠\\",
            size=32,
            weight=ft.FontWeight.W_600,
            color=catppuccin.PALETTE.frappe.colors.maroon.hex,
        )

        text = ft.Text(
            "Sorry, nothing to show here yet.",
            size=16,
        )

        self.content = ft.Column(
            [
                cat_text,
                text
            ],
            spacing=28,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    # @override
    @property
    def section_header(self):
        return "None"

    # @override
    @property
    def is_empty(self):
        return False
