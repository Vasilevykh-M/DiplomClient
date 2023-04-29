from Interface.SendFileForm import SendFile as SendForm
from Interface.GetPredictForm import GetPredict as GetPredictForn

import flet as ft

class MainApp(ft.UserControl):
    def __init__(self, accept):
        super(MainApp, self).__init__()
        self.accept = accept


    def build(self):
        self.snack_bar = ft.SnackBar(ft.Text("Выполнено"), bgcolor=ft.colors.GREEN, action="Alright!")
        self.tabs = ft.Tabs(tabs = [
            ft.Tab(text = "Отправить файл на сервер"),
            ft.Tab(text = "Получить прогноз"),
        ],
            on_change=self.on_select_tab
        )
        self.send_file_component = SendForm(self.accept)
        self.get_predict_component = GetPredictForn(self.accept)
        self.get_predict_component.visible = False
        return ft.Column(controls=[
            self.tabs,
            self.send_file_component,
            self.get_predict_component,
        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        width=1200,
                         )

    def on_select_tab(self, e):
        status = self.tabs.tabs[self.tabs.selected_index].text
        if status == "Отправить файл на сервер":
            self.send_file_component.visible = True
            self.get_predict_component.visible = False

        if status == "Получить прогноз":
            self.send_file_component.visible = False
            self.get_predict_component.visible = True

        self.update()

def main(page: ft.Page):
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Hello, world!"),
        action="Alright!",
    )


    def accept(code):
        if code == 1:
            page.snack_bar = ft.SnackBar(ft.Text("Выполнено"), bgcolor=ft.colors.GREEN)
        if code == -1:
            page.snack_bar = ft.SnackBar(ft.Text("Ошибка"), bgcolor=ft.colors.RED)
        page.snack_bar.open = True
        page.update()

    main_component = MainApp(accept)
    page.window_height = 600
    page.window_width = 1200
    page.window_resizable = False
    page.window_maximizable = False
    page.spacing = 50
    page.add(main_component)

ft.app(target=main)
