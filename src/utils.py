from typing import Callable

from components.todo import TodoModel


def create_filter_todos(filter_string: str) -> Callable[[TodoModel], bool]:
    def filter_todos(todo: TodoModel) -> bool:
        return todo.name.__contains__(filter_string)
    return filter_todos
