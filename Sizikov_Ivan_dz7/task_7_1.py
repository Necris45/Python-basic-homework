# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
# конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

from os import makedirs, mkdir
from os.path import abspath, join, exists

my_project_dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']
core_dir = "my_project"
if not exists(core_dir):
    mkdir(core_dir)
for folder in my_project_dir_list:
    if not exists(folder):
        makedirs(abspath(join(core_dir, folder)))
