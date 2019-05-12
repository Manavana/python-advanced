# Задание на закрепление знаний по модулю CSV
import os
import re
import csv


# Отображает файлы текущей директории
def show_files():
    f = os.listdir(path=os.getcwd())
    return f


# Извлекает информацию и записывает в соответствущий список
def search_info(regexp, element, info_list):
    res = re.search(regexp, element)
    r = res.group(0)
    info_list.append(r[:-1])


# Заполняет основной список названиями столбцов
def title_row(title, info_list):
    if title in info_list:
        pass
    else:
        info_list.append(title)


def get_data(name):
    pass
    """
    # в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных
    данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
    «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
    Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
    В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
    названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
    """


def write_to_csv():
    """
    В этой функции реализовать получение данных через вызов функции get_data(),
    а также сохранение подготовленных данных в соответствующий CSV-файл;
    """
    pass


files = show_files()

# Списки, где будет храниться извлекаемая из файлов информация
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

# Список с названиями столбцов
main_data_list = []

# Перебор циклом всех файлов, находящихся в директории, и открытие необходимых файлов
for file in files:
    if re.match('^info_*[0-9].txt$', file) is not None:
        with open(file) as f:
            # Чтение и поиск данных, а также раскидывание инфы по соответствующим спискам
            for line in f:
                if re.search('(?<=Изготовитель системы:\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line) is not None:
                    search_info('(?<=Изготовитель системы:\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line, os_prod_list)
                    title_row('Изготовитель системы', main_data_list)
                elif re.search('(?<=Название ОС:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line) is not None:
                    search_info('(?<=Название ОС:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line, os_name_list)
                    title_row('Название ОС', main_data_list)
                elif re.search('(?<=Код продукта:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line) is not None:
                    search_info('(?<=Код продукта:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line, os_code_list)
                    title_row('Код продукта', main_data_list)
                elif re.search('(?<=Тип системы:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line) is not None:
                    search_info('(?<=Тип системы:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line, os_type_list)
                    title_row('Тип системы', main_data_list)
                else:
                    continue

            # Итогом поиска являются списки с информацией
            # for line in f:
            #     if len(re.findall('(?:Изготовитель системы:)(?:\s+\S+)+', line)) > 0:
            #         os_prod_list.append(re.findall('(?:Изготовитель системы:)(?:\s+\S+)+', line))
            #     elif len(re.findall('(?:Название ОС:)(?:\s+\S+)+', line)) > 0:
            #         os_name_list.append(re.findall('(?:Название ОС:)(?:\s+\S+)+', line))
            #     elif len(re.findall('(?:Код продукта:)(?:\s+\S+)+', line)) > 0:
            #         os_code_list.append(re.findall('(?:Код продукта:)(?:\s+\S+)+', line))
            #     elif len(re.findall('(?:Тип системы:)(?:\s+\S+)+', line)) > 0:
            #         os_type_list.append(re.findall('(?:Тип системы:)(?:\s+\S+)+', line))
            #     else:
            #         pass

print(os_prod_list, os_name_list, os_code_list, os_type_list, main_data_list)
        # print(files.index(res.group(0)))
        # lst.append(file)