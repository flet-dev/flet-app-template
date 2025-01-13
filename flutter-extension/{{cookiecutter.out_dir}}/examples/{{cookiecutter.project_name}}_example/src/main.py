import flet as ft

from {{cookiecutter.project_name}} import {{cookiecutter.project_name.replace('-','_').split('_')|map('capitalize')|join}}


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Stack(
            [
                ft.Container(height=200, width=200, bgcolor=ft.colors.BLUE_100),
                {{cookiecutter.project_name.replace('-','_').split('_')|map('capitalize')|join}}(
                    opacity=0.5,
                    tooltip="My new control tooltip",
                    top=0,
                    left=0,
                    value = "My new Flet Control"
                    color=ft.Colors.RED,
                ),
            ]
        )
    )


ft.app(main)
