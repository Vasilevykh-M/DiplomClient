import flet as ft
import grpc
import pandas as pd

import RemouteSmartRieltor_pb2_grpc
import generator_data
import validation_data

def get_predict(data):
    return generator_data.create_generator_to_pred(data)

class GetPredict(ft.UserControl):

    def __init__(self, accept):
        super(GetPredict, self).__init__()
        self.accept = accept
        self.file_output = ""

    def save_file(self, e: ft.FilePickerResultEvent):
        self.output_file_name.value = "Выходной файл: " + e.path + ".xlsx"
        self.file_output = e.path + ".xlsx"

    def build(self):
        self.file_pickerAdd = ft.FilePicker(on_result=self.save_file)
        self.file_picker = ft.FilePicker(on_result=self.get_file_picker)
        self.output_file_button = ft.ElevatedButton("Создать файл для результатов", on_click=lambda _: self.file_pickerAdd.save_file(allowed_extensions=["xlsx"]))
        self.get_file = ft.ElevatedButton("Выбрать файл и получить прогноз", on_click=self.get_file_click)
        self.output_file_name = ft.Text("Выходной файл: ")
        return ft.Column(controls=
                         [
                             self.file_pickerAdd,
                             self.file_picker,
                             ft.Row(controls=[
                                 self.output_file_name
                             ],
                                 alignment=ft.MainAxisAlignment.CENTER,
                                 spacing=50,
                                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
                             ),
                             ft.Row(controls=[
                                 self.output_file_button,
                                 self.get_file,
                             ],
                                 alignment=ft.MainAxisAlignment.CENTER,
                                 spacing=50,
                                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
                             )],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            height=400,
            width=1200)

    def get_file_picker(self, e: ft.FilePickerResultEvent):
        if e.files != None:
            data = pd.read_excel(e.files[0].path)
            if validation_data.validation_(data, True):
                    data = validation_data.cleanMissingValues(data)
                    with grpc.insecure_channel('localhost:15000') as channel:
                        stub = RemouteSmartRieltor_pb2_grpc.ClientServiceStub(channel)
                        data = stub.getPredict(get_predict(data))
                        arr = []
                        for i in data:
                            arr.append(i.StateBooking)
                        data = pd.read_excel(e.files[0].path)
                        data["Результат"] = arr
                        print(data)
                        data.to_excel(self.file_output)
                        print("A")
                        self.accept(1)
            else:
                self.accept(-1)
        self.update()

    def get_file_click(self, e):
        self.file_picker.pick_files(allow_multiple=False, allowed_extensions=["xls", "xlsx"])