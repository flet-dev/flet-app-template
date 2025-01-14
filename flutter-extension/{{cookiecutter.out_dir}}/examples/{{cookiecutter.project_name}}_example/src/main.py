import flet as ft

from {{cookiecutter.project_name}} import {{cookiecutter.control_name}}


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Stack(
            [
                ft.Container(height=300, width=300, bgcolor=ft.colors.BLUE_100),
                {{cookiecutter.control_name}}(
                    opacity=0.5,
                    tooltip="My new control tooltip",
                    top=100,
                    left=0,
                    value = "My new {{cookiecutter.control_name}} Flet Control", 
                    color=ft.Colors.RED,
                ),
            ]
        )
    )


ft.app(main)
