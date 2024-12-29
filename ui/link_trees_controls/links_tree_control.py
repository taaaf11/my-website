from __future__ import annotations

from typing import override

import catppuccin
import flet as ft

from model import Link, AnimatableSectionABC


class LinkControl(ft.Container):
    def __init__(self, link: Link, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.link = link

        self.heading_colors = {
            'unvisited': catppuccin.PALETTE.frappe.colors.blue.hex,
            'visited': catppuccin.PALETTE.frappe.colors.lavender.hex,
        }

        heading = ft.Container(
            content=ft.Text(value=link.heading, size=21, weight=ft.FontWeight.W_500, color=self.heading_colors['unvisited']),
        )
        description = ft.Text(value=link.description)

        self.content = ft.Column(
            controls=[
                heading,
                description,
            ],
            tight=True,
            expand=False,
        )
        self.ink = True
        self.border = ft.border.all(
            1,
            catppuccin.PALETTE.frappe.colors.flamingo.hex
        )
        self.border_radius = 12
        self.padding = 15

        self.on_click = self._launch_link_url

    def _launch_link_url(self, _) -> None:
        self.page.launch_url(self.link.url)


class LinkTreeControl(ft.Container, AnimatableSectionABC):
    def __init__(self, links: list[Link], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.content = ft.ListView(
            controls=[
                LinkControl(link, margin=ft.padding.symmetric(vertical=10))
                for link in links
            ],
            divider_thickness=2
        )

    @override
    @property
    def section_header(self):
        return "Links"

    @override
    @property
    def is_empty(self):
        return False
