# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); Подумайте о возможных исключительных ситуациях при работе скрипта.
# Усложнение Библиотеки для парсинга yaml использовать нельзя.
from os import makedirs, mkdir, chdir
from os.path import abspath, join, exists

my_project_dir_list = ['settings', 'mainapp', 'adminapp']
py_settings_list = ["__init__.py", "dev.py", "prod.py"]
py_app_list = ["__init__.py", "models.py", "views.py"]
html_file_list = ["base.html", "index.html"]
core_dir = abspath(join("my_project"))
templates_dir = "templates"
if not exists(core_dir):
    mkdir(core_dir)
chdir(core_dir)
for folder in my_project_dir_list:
    if not exists(folder):
        makedirs(abspath(join(core_dir, folder)))
    if folder == 'settings':
        chdir(folder)
        for file in py_settings_list:
            with open(file, "w", encoding='utf-8') as my_file:
                pass
        chdir(core_dir)
    else:
        chdir(folder)
        for file in py_app_list:
            with open(file, "w", encoding='utf-8') as my_file:
                pass
        if not exists(abspath(join(templates_dir, folder))):
            makedirs(abspath(join(templates_dir, folder)))
        chdir(abspath(join(templates_dir, folder)))
        for file in html_file_list:
            with open(file, "w", encoding='utf-8') as my_file:
                pass
        chdir(core_dir)
