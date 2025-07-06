import random

import flet as ft


def main(page: ft.Page):
    todos = ft.ListView([ft.Text(random.random().__str__()) for _ in range(1000)], height=500, auto_scroll=True)
    new_task = ft.TextField("test")

    def add_todo(e):
        todos.controls.append(ft.Text(new_task.value))
        todos.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=add_todo
    )

    page.add(
        ft.SafeArea(
            ft.Container(
                new_task,
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        todos,
    )


ft.app(main)
