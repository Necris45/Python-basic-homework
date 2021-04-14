# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских
# папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная
# задача, которая решена, например, во фреймворке django.

from os import listdir
from os.path import abspath, join
from shutil import copytree

core_dir = abspath(join("my_project"))
copy_path = abspath(join(core_dir, "templates"))
for folder in listdir(core_dir):
    for inner_folder in listdir(abspath(join(core_dir, folder))):
        if inner_folder == "templates":
            source_path = abspath(join(core_dir, folder, inner_folder))
            copytree(src=source_path, dst=copy_path, dirs_exist_ok=True)
