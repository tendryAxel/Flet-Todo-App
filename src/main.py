import flet as ft


def main(page: ft.Page):
    todos = ft.ListView([])

    def add_todo(e):
        todos.controls.append(ft.Text(new_task.value))
        todos.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=add_todo
    )

    new_task = ft.TextField("test")
    page.add(
        ft.SafeArea(
            ft.Container(
                new_task,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


    page.add(todos)


ft.app(main)
