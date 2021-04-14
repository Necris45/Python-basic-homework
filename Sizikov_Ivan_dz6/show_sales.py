import sys
from task_6_4 import show_sales, how_much_str

if len(sys.argv) == 1:
    show_sales(start=1, stop=how_much_str())
elif len(sys.argv) == 2:
    show_sales(start=int(sys.argv[1]), stop=how_much_str())
elif len(sys.argv) == 3:
    show_sales(start=int(sys.argv[1]), stop=int(sys.argv[2]))
else:
    print('Вы ввели неверные данные.\n Нужно ввести не более 2 аргументов, первый из которых указывает начальную строку'
          ' для вывода, а второй - конечную.\nТакже можно не вводить аргументы для просмотра всего файла целиком или '
          'ввести только первый, чтобы смотреть весь файл с определенной строки.')
