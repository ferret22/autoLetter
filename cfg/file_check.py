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
        with open(path, 'w') as file:
            file.write(file_text)
        file.close()


class XlsxFiler:

    def open_xlsx(self, path: str):
        my_dict = pyexcel.get_dict(name_columns_by_row=0, file_name=path)

        counts = int(my_dict.get('Number')) + 1
        names = my_dict.get('Names')
        count_homework = my_dict.get('Homework')
        letter_flag = my_dict.get('Letter flag')

        with open('data.rcb', 'w') as file:
            file.write('Number\tNames\tHomework\tLetter flag')
            for i in range(counts):
                file.write(f'{i}\t{names[i]}\t{count_homework[i]}\t{letter_flag[i]}\n')
        file.close()

        return self._open_txt()

    @staticmethod
    def _open_txt():
        with open('data.rcb', 'r') as file:
            lines = file.readline()
            data = tuple(line.split('\t') for line in lines)
        file.close()

        return data


class Filer(DocxFiler, TxtFiler, XlsxFiler):  # Класс работы с файлами

    default_letter_good = 'cfg/defaultLetterGood.rcb'
    default_letter_bad = 'cfg/defaultLetterBad.rcb'

    @staticmethod
    def _read_letter(letter_file: str) -> str:  # Считывание любого файла письма
        with open(letter_file, 'r') as default_file:
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
        with open(letter_file, 'w') as file:
            file.write(letter_text)
        file.close()

    def write_letter(self, new_letter: str, flag: bool) -> None:  # Запись новых скриптов в дефолтные скрипты
        with open(new_letter, 'r') as new_file:
            letter = new_file.read()
        new_file.close()

        match flag:
            case True:
                self._write_text(self.default_letter_good, letter)
            case False:
                self._write_text(self.default_letter_bad, letter)
