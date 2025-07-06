import random
from collections.abc import Callable
from datetime import datetime

import flet as ft
from flet.core.control_event import ControlEvent


def create_filter_todos(filter_string: str) -> Callable[[ft.Text], bool]:
    def filter_todos(todo: ft.Text) -> bool:
        return todo.value.__contains__(filter_string)
    return filter_todos


todo_list = [ft.Text(random.random().__str__()) for _ in range(100)]
todo_list_to_display = todo_list

def main(page: ft.Page):
    global todo_list_to_display
    todos = ft.ListView(todo_list_to_display, height=500, auto_scroll=True)
    new_task = ft.TextField("test")

    def add_todo(e: ControlEvent):
        global todo_list_to_display
        todo_list_to_display = todo_list + [ft.Text(new_task.value)]
        update_todos_display()

    def filter_search(e: ControlEvent):
        global todo_list_to_display
        start = datetime.now()
        todo_list_to_display = list(filter(create_filter_todos(e.data), todo_list))
        end = datetime.now()
        print(f"Filter operation take: {end - start}")
        update_todos_display()

    def update_todos_display():
        todos.controls = todo_list_to_display
        todos.update()

    search_filter = ft.TextField(on_change=filter_search)

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
        ft.SafeArea(
            ft.Container(
                search_filter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        todos,
    )


ft.app(main)
