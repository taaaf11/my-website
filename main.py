import flet as ft


def name_container():
    name = ft.Text("Muhammad Altaaf", weight=ft.FontWeight.W_600, size=25)
    detail = ft.Text("A university undergraduate, persuading computer science major.", size=16)
    picture = ft.CircleAvatar(
        background_image_url='https://avatars.githubusercontent.com/u/109919009?v=4',
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


def main(page: ft.Page):
    page.title = "About me"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {
        'Inter': "assets/fonts/Inter-VariableFont_opsz,wght.ttf",
    }
    page.theme = ft.Theme(font_family='Inter')

    page.add(
        ft.Container(
            name_container(),
            width=page.window.width - 200,
            margin=ft.margin.symmetric(vertical=80),
        ),
    )

ft.app(main, assets_dir='assets')