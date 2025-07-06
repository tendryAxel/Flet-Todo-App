import faker
import flet as ft

from components.todo import TodoList, TodoModel


faker = faker.Faker()


def main(page: ft.Page):
    todo_list = TodoList([TodoModel(faker.sentence(10), faker.sentence(100)) for _ in range(100)])

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
