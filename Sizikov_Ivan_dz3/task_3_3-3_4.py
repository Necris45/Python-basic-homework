# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
def thesaurus(*args):
    thesaurus_dict = {}
    for name in args:
        if name[0] in thesaurus_dict:
            thesaurus_dict[name[0]].append(name)
        else:
            thesaurus_dict[name[0]] = [name]
    print(sorted(thesaurus_dict.items()))


thesaurus('Влад', 'Иван', 'Сергей', 'Елена', 'Мария', 'Василий', 'Василиса')


# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
#            "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
# {
#    'А':{
#           'П': ['Петр Алексеев']},
#    'И': {
#           'И': ['Илья Иванов']},
#    'С': {
#           'А': ['Алла Сидорова', 'Анна Савельева'],
#           'В': ['Василий Суриков'],
#           'И': ['Иван Сергеев', 'Инна Серова']}}
# Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus_adv(*args):
    thesaurus_adv_dict = {}
    for el in args:
        name = el.split(' ')
        temp_name_dict = {}
        if name[1][0] in thesaurus_adv_dict:
            if name[0][0] in thesaurus_adv_dict[name[1][0]]:
                thesaurus_adv_dict[name[1][0]][name[0][0]].append(el)
            else:
                temp_name_dict[name[0][0]] = [el]
                thesaurus_adv_dict[name[1][0]].update(temp_name_dict)
        else:
            temp_name_dict[name[0][0]] = [el]
            thesaurus_adv_dict[name[1][0]] = temp_name_dict
    for key in thesaurus_adv_dict.keys():
        if len(thesaurus_adv_dict[key]) > 1:
            thesaurus_adv_dict[key] = sorted(thesaurus_adv_dict[key].items())
    print(sorted(thesaurus_adv_dict.items()))


thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
              "Василий Суриков")
