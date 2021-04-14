# 4. Создать список, содержащий цены на товары (10 – 20 товаров), например:
# [57.8, 46.51, 97, ...]
# - Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

price_list = [57.8, 46.51, 97, 48.15, 34.03, 12.1, 77.65, 69.01, 52.06, 83.65]
id_before = id(price_list)
price_txt = ''
for idx, price in enumerate(price_list):
    rub = int(price)
    kop = int(100 * round((price - rub), 2))
    if idx != len(price_list) - 1:
        price_txt += f'{rub} руб {kop:02d} коп, '
    else:
        price_txt += f'{rub} руб {kop:02d} коп'
print(price_txt)

# - Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
# сортировки остался тот же).

price_list.sort()
price_txt_ascending = ''
for idx, price in enumerate(price_list):
    rub = int(price)
    kop = int(100 * round((price - rub), 2))
    if idx != len(price_list) - 1:
        price_txt_ascending += f'{rub} руб {kop:02d} коп, '
    else:
        price_txt_ascending += f'{rub} руб {kop:02d} коп'
print(price_txt_ascending)
id_after = id(price_list)
if id_before == id_after:
    print(f'ID списка до сортировки был {id_before}, ID после сортировки остался {id_after}')

# - Создать новый список, содержащий те же цены, но отсортированные по убыванию.

price_list_descending = sorted(price_list, reverse=True)
print(price_list_descending)

# - Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
# price_list[-5::1] в 45 строке можно заменить на price_list_descending[4::-1]
price_txt_highest_five = ''
for idx, price in enumerate(price_list[-5::1]):
    rub = int(price)
    kop = int(100 * round((price - rub), 2))
    if idx != 4:
        price_txt_highest_five += f'{rub} руб {kop:02d} коп, '
    else:
        price_txt_highest_five += f'{rub} руб {kop:02d} коп'
print(price_txt_highest_five)
