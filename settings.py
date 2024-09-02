from PySide2.QtWidgets import QWidget, QErrorMessage, QMessageBox
from ui.ui_py.settings_win import Ui_SettingsWin
from cfg.file_check import Filer
import tkinter as tk
from tkinter.filedialog import askopenfilename


class SettingsWin(QWidget, Filer):

    def __init__(self, screen_geometry: tuple[int, int], parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsWin()
        self.ui.setupUi(self)

        self.error = QErrorMessage(self)
        self.msg_info = QMessageBox(self)

        self.setMinimumSize(700, 330)
        self.setMaximumSize(screen_geometry[0], screen_geometry[1])

        self.ui.buttonLoadBad.clicked.connect(self.save_bad_letter)
        self.ui.buttonLoadGood.clicked.connect(self.save_good_letter)

    def show_msg_info(self, msg: str, title: str):  # Создание окна информации
        self.msg_info.setWindowTitle(title)
        self.msg_info.setText(msg)
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.show()

    def ms_error(self, title: str, message: str, type_error: str):  # Создание окна ошибки
        self.error.setWindowTitle(title)
        self.error.showMessage(message, type_error)

    def save_bad_letter(self):
        root = tk.Tk()
        root.withdraw()

        filetypes = (("Файл блокнота", "*.txt"),)
        path = askopenfilename(filetypes=filetypes, title="Открыть файл", initialdir="/")

        try:
            self.write_letter(path, False)
            self.show_msg_info('Файл сохранен! Можете закрывать окно!', 'Файл сохранен')
        except FileNotFoundError:
            self.ms_error('Не найден файл сохранения!', 'Не найден файл сохранения!\nПовторите попытку',
                          'FileNotFoundError')

    def save_good_letter(self):
        root = tk.Tk()
        root.withdraw()

        filetypes = (("Файл блокнота", "*.txt"),)
        path = askopenfilename(filetypes=filetypes, title="Открыть файл", initialdir="/")

        try:
            self.write_letter(path, True)
            self.show_msg_info('Файл сохранен! Можете закрывать окно!', 'Файл сохранен')
        except FileNotFoundError:
            self.ms_error('Не найден файл сохранения!', 'Не найден файл сохранения!\nПовторите попытку',
                          'FileNotFoundError')
