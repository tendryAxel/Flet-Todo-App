import random

import flet as ft

from components.todo import TodoList, TodoModel


def main(page: ft.Page):
    todo_list = TodoList([TodoModel(random.random().__str__(), random.random().__str__()) for _ in range(100)])

    page.add(
        ft.SafeArea(
            ft.Container(
                todo_list,
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
    )


ft.app(main)
