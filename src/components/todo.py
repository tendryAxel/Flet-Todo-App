from datetime import datetime

import flet as ft
from flet.core.control_event import ControlEvent

from utils import create_filter_todos


class TodoList(ft.Column):
    def __init__(self, default_todos: list):
        super().__init__()
        self.todo_list = default_todos
        self.todo_list_to_display = self.todo_list
        self.todos = ft.ListView(self.todo_list_to_display, height=500, auto_scroll=True)
        self.new_task = ft.TextField("test")
        self.search_filter = ft.TextField(on_change=self.filter_search)
        self.controls = [
            ft.Row([
                self.new_task,
                ft.FloatingActionButton(
                    icon=ft.Icons.ADD, on_click=self.add_todo
                ),
            ]),
            self.search_filter,
            self.todos,
        ]


    def add_todo(self, e: ControlEvent):
        self.todo_list.append(ft.Text(self.new_task.value))
        self.todo_list_to_display = self.todo_list
        self.update_todos_display()

    def filter_search(self, e: ControlEvent):
        start = datetime.now()
        self.todo_list_to_display = list(filter(create_filter_todos(e.data), self.todo_list))
        end = datetime.now()
        print(f"Filter operation take: {end - start}")
        self.update_todos_display()

    def update_todos_display(self):
        self.todos.controls = self.todo_list_to_display
        self.todos.update()
