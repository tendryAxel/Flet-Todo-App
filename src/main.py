import flet as ft


class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()

def main(page: ft.Page):
    task = ft.Text("0", size=50, data=0)

    def increment_click(e):
        task.value = new_task.value
        task.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
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

    page.add(
        ft.SafeArea(
            ft.Container(
                task,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
