from collections.abc import Callable

import catppuccin
import flet as ft

from model import AnimatableSectionProtocol


class SectionsHolderControl(ft.Container):
    def __init__(self, sections: list[AnimatableSectionProtocol]):
        super().__init__()
        self.sections = sections

        self.tabs = [
            ft.Container(
                ft.Text(section.section_header),
                ink=True,
                padding=13,
                border_radius=12,
                data=section.section_header,
                on_click=self._on_section_button_click
            )
            for section in sections
        ]

        self.main_content = ft.AnimatedSwitcher(
            sections[0],
            duration=300,
            reverse_duration=300,
        )

        self.content = ft.Column(
            controls=[
                ft.Row(self.tabs, alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(ft.Divider(thickness=1), width=200),
                self.main_content,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.alignment = ft.alignment.center
        # self.border = ft.border.all(1)

    def did_mount(self):
        first_tab = self.tabs[0]

        first_tab.bgcolor = catppuccin.PALETTE.frappe.colors.pink.hex
        first_tab.content.color = catppuccin.PALETTE.frappe.colors.crust.hex
        first_tab.update()

    def _on_section_button_click(self, e):
        section: AnimatableSectionProtocol
        e.control: ft.Container

        for section in self.sections:
            is_true_section = section.section_header == e.control.data

            for tab in self.tabs:
                tab.bgcolor = ft.Colors.TRANSPARENT
                tab.content.color = None

            if is_true_section:
                # updating tab color
                e.control.bgcolor = "#E6" + catppuccin.PALETTE.frappe.colors.pink.hex[1:]
                e.control.content.color = catppuccin.PALETTE.frappe.colors.crust.hex
                e.control.update()

                # updating section content
                self.main_content.content = section
                self.update()
