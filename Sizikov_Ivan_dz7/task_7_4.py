# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя
# граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

from os import scandir, walk
from os.path import abspath, join, isfile

size_list = [10, 100, 1000, 10000, 100000]
size_dict = {}
size_dict_sorted = {}
root_dir = abspath(join("my_project"))  # Для указания папки, в которой будем работать.
for address, dirs, files in walk(root_dir):
    for file in scandir(address):
        if isfile(file):
            for index in range(0, len(size_list)):
                if index == 0:
                    if file.stat().st_size <= size_list[index]:
                        if size_list[index] not in size_dict:
                            size_dict[size_list[index]] = 0
                        size_dict[size_list[index]] += 1
                else:
                    if size_list[index - 1] < file.stat().st_size <= size_list[index]:
                        if size_list[index] not in size_dict:
                            size_dict[size_list[index]] = 0
                        size_dict[size_list[index]] += 1
list_keys = list(size_dict.keys())
list_keys.sort()
for key in list_keys:
    size_dict_sorted[key] = size_dict[key]
print(size_dict_sorted)
