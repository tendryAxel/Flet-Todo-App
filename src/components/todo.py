from dataclasses import dataclass
from datetime import datetime
from typing import List, AnyStr

import flet as ft
from flet.core.control_event import ControlEvent


@dataclass
class TodoModel:
    name: str
    description: str

    @staticmethod
    def filter(todos: List["TodoModel"], filter_string: AnyStr) -> List["TodoModel"]:
        return [todo for todo in todos if todo.name.__contains__(filter_string)]


class TodoListItem(ft.Row):
    def __init__(self, todo: TodoModel):
        super().__init__()
        self.todo = todo
        self.controls = [
            ft.Text(todo.name),
            ft.Text(todo.description),
        ]

    @staticmethod
    def from_todo(todo: TodoModel) -> "TodoListItem":
            return TodoListItem(todo)

    @staticmethod
    def from_todos(todos: list[TodoModel]) -> List["TodoListItem"]:
            return [TodoListItem.from_todo(todo) for todo in todos]


class TodoList(ft.Column):
    def __init__(self, default_todos: list[TodoModel]):
        super().__init__()
        self.todo_list: list[TodoModel] = default_todos
        self.todo_list_to_display: list[TodoModel] = self.todo_list
        self.todos = ft.ListView(TodoListItem.from_todos(self.todo_list_to_display), height=500, auto_scroll=True)
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
        self.todo_list.append(TodoModel(self.new_task.value, ""))
        self.todo_list_to_display = self.todo_list
        self.update_todos_display()

    def filter_search(self, e: ControlEvent):
        start = datetime.now()
        self.todo_list_to_display = TodoModel.filter(self.todo_list, e.data)
        end = datetime.now()
        print(f"Filter operation take: {end - start}")
        self.update_todos_display()

    def update_todos_display(self):
        self.todos.controls = TodoListItem.from_todos(self.todo_list_to_display)
        self.todos.update()
