from PySide2.QtWidgets import *
from ui.ui_py.main_win import Ui_MainWinLetter
from cfg.file_check import Filer
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from settings import SettingsWin


class ProgramWindow(QMainWindow, Filer):

    def __init__(self, width: int, height: int, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWinLetter()
        self.ui.setupUi(self)

        self.screen_geometry = (width, height)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(width, height)

        self.error = QErrorMessage(self)
        self.msg_info = QMessageBox(self)

        self.letter_good = ''
        self.letter_bad = ''
        self.data = tuple()

        self.ui.buttonSaveLetters.clicked.connect(self.save_text)
        self.ui.buttonReloadLetters.cliced.connect(self.update_letters)
        self.ui.actionSettings.triggered.connect(self.open_settings)
        self.ui.actionOpen.triggered.connect(self.load_xlsx_file)

        self.check_letters()

    def show_msg_info(self, msg: str, title: str):  # Создание окна информации
        self.msg_info.setWindowTitle(title)
        self.msg_info.setText(msg)
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.show()

    def ms_error(self, title: str, message: str, type_error: str):  # Создание окна ошибки
        self.error.setWindowTitle(title)
        self.error.showMessage(message, type_error)

    def save_docx_file(self, text: str):
        root = tk.Tk()
        root.withdraw()

        filetypes = (("Word документ", "*.docx"),)
        path = asksaveasfilename(filetypes=filetypes, title="Сохранить файл", initialdir="/",
                                 initialfile='example.docx')

        try:
            self.save_docx(path, text)
            self.show_msg_info('Файл сохранен! Можете закрывать окно!', 'Файл сохранен')
        except FileNotFoundError:
            self.ms_error('Не найден файл сохранения!', 'Не найден файл сохранения!\nПовторите попытку',
                          'FileNotFoundError')

    def save_txt_file(self, text: str):
        root = tk.Tk()
        root.withdraw()

        filetypes = (("Файл блокнота", "*.txt"),)
        path = asksaveasfilename(filetypes=filetypes, title="Сохранить файл", initialdir="/",
                                 initialfile='example.txt')

        try:
            self.save_txt(path, text)
            self.show_msg_info('Файл сохранен! Можете закрывать окно!', 'Файл сохранен')
        except FileNotFoundError:
            self.ms_error('Не найден файл сохранения!', 'Не найден файл сохранения!\nПовторите попытку',
                          'FileNotFoundError')

    def save_text(self):
        if self.ui.radioSaveTXT.isChecked():
            pass

        if self.ui.radioSaveDOCX.isChecked():
            pass

    def open_settings(self):
        self.settings_win = SettingsWin(self.screen_geometry)
        self.settings_win.show()

    def update_letters(self):
        self.letter_good, self.letter_bad = self.load_letters()

    def load_xlsx_file(self):
        root = tk.Tk()
        root.withdraw()

        filetypes = (("Excel таблица", "*.xlsx"),)
        path = askopenfilename(filetypes=filetypes, title="Открыть файл", initialdir="/")

        try:
            self.data = self.open_xlsx(path)
            self.show_msg_info('Файл загружен! Можете закрывать окно!', 'Файл загружен')
            self.ui.textStudentsList.setText('')
            self.ui.lineStudentsNum.setText('')

            text = ''
            for line in self.data:
                string = ''
                for word in line:
                    string += word + '\t'
                text += string + '\n'

            self.ui.textStudentsList.setText(text)
            self.ui.lineStudentsNum.setText(str(len(self.data)))

        except FileNotFoundError:
            self.ms_error('Не найден файл загрузки!', 'Не найден файл загрузки!\nПовторите попытку',
                          'FileNotFoundError')

    def check_letters(self):  # Проверка установки дефолтных скриптов
        if not self.check_default():
            self.ms_error('Нет скрипта для писем!',
                          'Нет скриптов для писем!\nЗагрузите их через меню "Settings"', 'No file')
        else:
            self.update_letters()
            self.show_msg_info('Скрипты обновлены! Можете закрывать окно!', 'Обновление скриптов')
