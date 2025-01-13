import flet as ft

from flet_spinkit import Spinkit, SpinkitType


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Stack(
            [
                ft.Container(height=200, width=200, bgcolor=ft.colors.BLUE_100),
                Spinkit(
                    opacity=0.5,
                    tooltip="Spinkit tooltip",
                    top=0,
                    left=0,
                    color=ft.Colors.RED,
                    size=150,
                    spinkit_type=SpinkitType.FOLDING_CUBE,
                ),
            ]
        )
    )


ft.app(main)
