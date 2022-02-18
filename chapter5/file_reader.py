from os.path import exists
from yaml import safe_load_all, safe_load
from xlrd import open_workbook
from configparser import ConfigParser


class File:

    def __init__(self, file_path: str):
        if not exists(file_path):
            raise FileNotFoundError
        self._file_path = file_path
        self._data = None


class YamlReader(File):

    def __init__(self, yml_path: str, multi: bool = False):
        super(YamlReader, self).__init__(yml_path)
        self._multi = multi

    @property
    def data(self):
        if not self._data:
            with open(self._file_path, 'rb') as fp:
                if self._multi:
                    self._data = list(safe_load_all(fp))
                else:
                    self._data = safe_load(fp)
        return self._data


class ExcelReader(File):

    def __init__(self,
                 excel_path: str,
                 sheet: [str, int],
                 excel_title: bool = True):
        """
        A  B  C
        A1 B1 C1
        A2 B2 C2

        ExcelReader(path, sheet=0).data
        [{A: A1, B: B1, C: C1}, {A: A2, B: B2, C: C2}]

        ExcelReader(path, sheet=0, excel_title=False).data
        [[A1, B1, C1], [A2, B2, C2]]
        :param excel_path:
        :param sheet:
        :param excel_title:
        """
        super(ExcelReader, self).__init__(excel_path)
        self._sheet = sheet
        self._excel_title = excel_title
        self._data = []

    @property
    def data(self):
        if not self._data:
            work_book = open_workbook(self._file_path)
            if not isinstance(self._sheet, (int, str)):
                raise TypeError(
                    'excel文件的表格：{}不存在'.format(self._sheet)
                )
            if isinstance(self._sheet, int):
                s = work_book.sheet_by_index(self._sheet)
            else:
                s = work_book.sheet_by_name(self._sheet)

            if self._excel_title:
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))

        return self._data


# obj = YamlReader(r'D:\Program Files\JetBrains\imooc\chapter5\demo.yml')
# print(obj.data)
# obj = ExcelReader(r'D:\Program Files\JetBrains\imooc\chapter5\demo.xlsx',
#                   sheet=0, excel_title=False).data
# print(obj)


class INIReader(File):

    def __init__(self, ini_path: str, section: str = 'MYSQL'):
        super(INIReader, self).__init__(ini_path)
        self._data = {}
        self._section = section.upper()
        self._parser = ConfigParser()

    @property
    def data(self):
        if not self._data:
            self._parser.read(self._file_path, encoding='UTF-8')
            for k, v in self._parser.items(self._section):
                self._data[k] = int(v) if k in ('port', 'maxsize', 'minsize', 'max', 'min', 'increment') else v
        return self._data


# ini = INIReader(r'D:\Program Files\JetBrains\imooc\chapter8\database.ini', 'oracle').data
# print(ini)
