import catppuccin
from catppuccin import PALETTE
import flet as ft


from model import Link, MusicData, ContactData
from ui.contact_section import ContactSection
from ui.link_trees_controls.projects_links_tree_control import ProjectLinksTreeControl
from ui.music_section_control import MusicSectionControl
from ui.sections_holder_control import SectionsHolderControl

# source for assets/gray0_ctp_on_line.svg: https://github.com/catppuccin/catppuccin/blob/main/assets/footers/gray0_ctp_on_line.svg


def name_container() -> ft.Control:
    name = ft.Text("Muhammad Altaaf", weight=ft.FontWeight.W_900, size=25)
    detail = ft.Text("A university undergraduate, pursuing computer science major.", size=16)
    picture = ft.CircleAvatar(
        background_image_src='https://avatars.githubusercontent.com/u/109919009?v=4',
        radius=35,
    )

    name_detail_col = ft.Column(
        [
            name,
            detail,
        ]
    )

    full_control = ft.Row(
        [
            name_detail_col,
            picture,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    return full_control


def made_with_heart(color: str) -> ft.Control:
    return ft.Text(
        spans=[
            ft.TextSpan("Made with "),
            ft.TextSpan("", style=ft.TextStyle(font_family="Symbols-NF")),
            ft.TextSpan(" and "),
            ft.TextSpan("", style=ft.TextStyle(font_family="Symbols-NF")),
        ],
        color=color,
    )


def main(page: ft.Page) -> None:
    page.scroll = ft.ScrollMode.AUTO
    use_palette = PALETTE.frappe

    page.title = "About me"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = use_palette.colors.crust.hex

    page.fonts = {
        'Inter': "fonts/Inter-VariableFont_opsz,wght.ttf",
        'Comfortaa': "fonts/Comfortaa[wght].ttf",
        'Symbols-NF': "fonts/SymbolsNerdFont-Regular.ttf"
    }
    # page.theme = ft.Theme(font_family='Inter')
    page.theme = ft.Theme(font_family='Comfortaa')

    contact_datas = [
        ContactData(
            icon_char="",
            heading="Discord",
            username="@taafu",
            url="https://www.discord.com",
            card_color=catppuccin.PALETTE.frappe.colors.lavender.hex,
        ),
        ContactData(
            icon_char="",
            heading="Mail",
            username="taafuuu@gmail.com",
            url="mailto:taafuuu@gmail.com",
            card_color=catppuccin.PALETTE.frappe.colors.flamingo.hex,
        ),
    ]

    page.add(
        ft.Container(
            ft.Column(
                controls=[
                    name_container(),
                    SectionsHolderControl(
                        [
                            ProjectLinksTreeControl(Link.from_data_file('projects_data.toml')),
                            MusicSectionControl(musics_data=MusicData.from_data_file()),
                            ContactSection(contact_datas),
                        ]
                    ),
                ],
                spacing=50,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=page.width - 200,
            margin=ft.margin.symmetric(vertical=80),
            expand=True,
        ),
        ft.Image(
            src="gray0_ctp_on_line.svg",
            color=catppuccin.PALETTE.frappe.colors.pink.hex,
            opacity=1.0,
        ),
        made_with_heart(catppuccin.PALETTE.frappe.colors.rosewater.hex,)
    )

ft.app(
    main,
    assets_dir='assets',
    view=ft.AppView.WEB_BROWSER
)
