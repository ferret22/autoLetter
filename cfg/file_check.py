import docx
from docx.shared import Pt
import pyexcel
from pyexcel._compact import OrderedDict


class DocxFiler:  # Класс записи писем в *.docx файлы

    doc = docx.Document()
    _style = doc.styles['Normal']
    _style.font.name = 'Times New Roman'
    _style.font.size = Pt(14)

    def save_docx(self, path: str, file_text: str) -> None:
        self.doc.add_paragraph(file_text)
        self.doc.save(path)


class TxtFiler:  # Класс записи писем в *.txt файлы

    @staticmethod
    def save_txt(path: str, file_text: str) -> None:
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(file_text)
        file.close()


class XlsxFiler:

    def open_xlsx(self, path: str):
        my_dict = pyexcel.get_dict(name_columns_by_row=0, file_name=path)

        counts = my_dict.get('Номер')
        full_names = my_dict.get('ФИО')
        count_skipping = my_dict.get('Кол-во пропусков')
        count_homework = my_dict.get('Сдача ДЗ')
        problems = my_dict.get('Проблемы')
        problems_description = my_dict.get('Описание проблемы')
        solutions = my_dict.get('Решение проблемы')

        with open('data.rcb', 'w', encoding='UTF-8') as file:
            file.write('Номер\tФИО\tКол-во пропусков\tСдача ДЗ\tПроблемы\tОписание проблемы\tРешение проблемы\n')
            for i in range(len(counts)):
                file.write(f'{i + 1}\t{full_names[i]}\t{count_skipping[i]}\t{count_homework[i]}\t{problems[i]}'
                           f'\t{problems_description[i]}\t{solutions[i]}\n')
        file.close()

        return self._open_txt()

    @staticmethod
    def _open_txt():
        with open('data.rcb', 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            data = tuple(line.split('\t') for line in lines)
        file.close()

        return data


class Filer(DocxFiler, TxtFiler, XlsxFiler):  # Класс работы с файлами

    default_letter_good = 'cfg/defaultLetterGood.rcb'
    default_letter_bad = 'cfg/defaultLetterBad.rcb'

    @staticmethod
    def _read_letter(letter_file: str) -> str:  # Считывание любого файла письма
        with open(letter_file, 'r', encoding='UTF-8') as default_file:
            letter = default_file.read()
        default_file.close()

        return letter

    def check_default(self) -> bool:  # Проверка установки дефолтных скриптов
        letter_good = self._read_letter(self.default_letter_good)
        letter_bad = self._read_letter(self.default_letter_bad)

        if len(letter_good) > 0 and len(letter_bad) > 0:
            return True
        return False

    def load_letters(self) -> tuple[str, str]:  # Загрузка дефолтных скриптов
        letter_good = self._read_letter(self.default_letter_good)
        letter_bad = self._read_letter(self.default_letter_bad)

        return letter_good, letter_bad

    @staticmethod
    def _write_text(letter_file: str, letter_text: str) -> None:  # Запись текста в файла
        with open(letter_file, 'w', encoding='UTF-8') as file:
            file.write(letter_text)
        file.close()

    def write_letter(self, new_letter: str, flag: bool) -> None:  # Запись новых скриптов в дефолтные скрипты
        with open(new_letter, 'r', encoding='UTF-8') as new_file:
            letter = new_file.read()
        new_file.close()

        match flag:
            case True:
                self._write_text(self.default_letter_good, letter)
            case False:
                self._write_text(self.default_letter_bad, letter)
