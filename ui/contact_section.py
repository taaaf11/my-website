import catppuccin
import flet as ft

from model import SectionABC, ContactData


class SingleContact(ft.Container):
    def __init__(self, contact_data: ContactData, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.contact_data = contact_data
        self.content = ft.Column(
            [
                ft.Container(
                    ft.Text(contact_data.icon_char, font_family="Symbols-NF", size=20),
                    border_radius=10,
                    bgcolor=contact_data.card_color,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Container(
                    ft.Column(
                        [
                            ft.Text(contact_data.heading, weight=ft.FontWeight.W_700, size=17),
                            ft.Text(contact_data.username),
                        ],
                        spacing=0,
                    )
                )
            ]
        )

        self.bgcolor = catppuccin.PALETTE.frappe.colors.mantle.hex

        self.height = 180
        self.width = 200

        self.border_radius = 10
        self.padding = 15

        self.animate_scale = 150

        self.on_click = lambda _: self.page.launch_url(contact_data.url)
        self.on_hover = self.inc_dec_scale
        # self.border = ft.border.all(1)

    def inc_dec_scale(self, e):
        if e.data == "true":
            self.scale = 1.1
            self.update()
        else:
            self.scale = 1.0
            self.update()


class ContactSection(ft.Container, SectionABC):
    def __init__(self, contact_datas: list[ContactData], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.contact_datas = contact_datas
        self.content = [
            SingleContact(contact_data)
            for contact_data in contact_datas
        ]

    @property
    def section_header(self) -> str:
        return "Contact"

    @property
    def is_empty(self) -> bool:
        return not bool(self.contact_datas)
