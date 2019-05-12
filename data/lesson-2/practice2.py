# Задание на закрепление знаний по модулю CSV
import os
import re
import numpy as np
import csv


# Отображает файлы текущей директории
def show_files():
    f = os.listdir(path=os.getcwd())
    return f

'''
Извлекает информацию и записывает в соответствущий список.

К сожалению, более изящного решения я пока не нашла, кроме как по-тупому посчитать кол-во пробелов в файле и добавить 
именно столько в регулярное выражение, после чего отрезать знак перевода строки.
Для автоматизации и дальнейшего масштабирования, алгоритм нужно переработать.
'''
def search_info(regexp, element, info_list):
    res = re.search(regexp, element)
    r = res.group(0)
    info_list.append(r[:-1])


'''
Заполняет основной список названиями столбцов. Этот отдельный список с названиями необходим для того, чтобы многократно 
не добавлялись названия в список, если файлов будет много более трех.
'''
def title_row(title, info_list, name_list):
    if title in info_list:
        pass
    else:
        info_list.append(title)
        name_list.insert(0, title)


# Собирает все данные для записи в файл, преобразует в массив и транспонирует
def collect_data(main_list, *args):
    main_list.append(list(args))
    arr = np.array(main_list[0])
    arr_trans = arr.T
    return arr_trans


def get_data():
    """
    # В цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных
    данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
    «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
    Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
    В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
    названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
    """
    files = show_files()

    # Списки, где будет храниться извлекаемая из файлов информация
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    # Список с названиями столбцов и всеми данными
    main_data_list = []
    main_data = []

    # Перебор циклом всех файлов, находящихся в директории, и открытие необходимых файлов
    for file in files:
        if re.match('^info_*[0-9].txt$', file) is not None:
            with open(file) as f:
                # Чтение и поиск данных, а также раскидывание инфы по соответствующим спискам
                for line in f:
                    if re.search('(?<=Изготовитель системы:\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line) is not None:
                        search_info('(?<=Изготовитель системы:\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line,
                                    os_prod_list)
                        title_row('Изготовитель системы', main_data_list, os_prod_list)
                    elif re.search('(?<=Название ОС:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+',
                                   line) is not None:
                        search_info('(?<=Название ОС:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line,
                                    os_name_list)
                        title_row('Название ОС', main_data_list, os_name_list)
                    elif re.search('(?<=Код продукта:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+',
                                   line) is not None:
                        search_info('(?<=Код продукта:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line,
                                    os_code_list)
                        title_row('Код продукта', main_data_list, os_code_list)
                    elif re.search('(?<=Тип системы:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+',
                                   line) is not None:
                        search_info('(?<=Тип системы:\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s)(?:\S+\s)+', line,
                                    os_type_list)
                        title_row('Тип системы', main_data_list, os_type_list)
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

    a = collect_data(main_data, os_name_list, os_code_list, os_prod_list, os_type_list)
    return a


def write_to_csv():
    """
    В этой функции реализовать получение данных через вызов функции get_data(),
    а также сохранение подготовленных данных в соответствующий CSV-файл;
    """
    data = get_data()

    with open('data.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)


write_to_csv()
with open('data.csv') as f_n:
    print(f_n.read())

