import sys
from task_6_4 import add_sale

if len(sys.argv) != 2:
    print('Вы не ввели добавляемое значение или ввели лишнее значение')
else:
    add_sale(sys.argv[1])
