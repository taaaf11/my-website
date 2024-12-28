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

    def _on_section_button_click(self, e):
        section: AnimatableSectionProtocol
        for section in self.sections:
            is_true_section = section.section_header == e.control.data
            if is_true_section:
                self.main_content.content = section
                self.update()
