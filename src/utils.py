from typing import Callable

import flet as ft


def create_filter_todos(filter_string: str) -> Callable[[ft.Text], bool]:
    def filter_todos(todo: ft.Text) -> bool:
        return todo.value.__contains__(filter_string)
    return filter_todos
