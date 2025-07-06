import flet as ft

class InputText(ft.Row):
    def __init__(self, title: str, input_component: ft.TextField):
        super().__init__()
        self.title = ft.Text(title)
        self.input_component = input_component
        self.controls = [
            self.title,
            self.input_component,
        ]

    @property
    def value(self):
        return self.input_component.value

