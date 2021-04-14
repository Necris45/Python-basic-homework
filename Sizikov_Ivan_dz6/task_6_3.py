# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о
# хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО значение в
# словаре - None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1». Примечание:
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import json

users_hobby_dict = {}
with open('users.csv', 'r', encoding='utf-8') as users_file:
    users_list = []
    for line in users_file:
        temp_list = line.split(",")
        users_value = ''
        for el in temp_list:
            if el == temp_list[0]:
                users_value += el
            elif el[-1] == '\n':
                users_value += f' {el[:-1]}'
            else:
                users_value += f' {el}'
        users_list.append(users_value)

with open('hobby.csv', 'r', encoding='utf-8') as hobby_file:
    hobby_list = []
    for line in hobby_file:
        temp_list = line.split(",")
        if temp_list[-1][-1] == '\n':
            temp_list[-1] = temp_list[-1][:-1]
        temp_hobby = ''
        for hobby in temp_list:
            if hobby == temp_list[0]:
                temp_hobby += hobby
            else:
                temp_hobby += f', {hobby}'
        hobby_list.append(temp_hobby)
if len(users_list) >= len(hobby_list):
    for i in range(0, len(users_list)):
        if i >= len(hobby_list):
            users_hobby_dict[users_list[i]] = None
        else:
            users_hobby_dict[users_list[i]] = hobby_list[i]
    with open('User_hobby_dict.csv', 'w', encoding='utf-8') as user_hobby_dict_file:
        json.dump(users_hobby_dict, user_hobby_dict_file, indent=2, ensure_ascii=False)
else:
    for i in range(0, len(users_list)):
        users_hobby_dict[users_list[i]] = hobby_list[i]
    with open('User_hobby_dict.csv', 'w', encoding='utf-8') as user_hobby_dict_file:
        json.dump(users_hobby_dict, user_hobby_dict_file, indent=2, ensure_ascii=False)
    raise SystemExit(1)
