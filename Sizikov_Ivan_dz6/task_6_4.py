# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных.
# Данные хранить в файле bakery.csv в кодировке utf-8.
# При записи передавать из командной строки значение суммы продаж. Новая запись дозаписывается в конец файла.
# # Для чтения данных реализовать в командной строке следующую логику. Предполагаем, что первая запись имеет номер 1.
# 1) просто запуск скрипта — выводить все записи;
# 2) запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# 3) запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный
# второму числу, включительно;
# Примеры запуска скриптов:
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
# Усложнение Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

def add_sale(value):
    with open('bakery.csv', 'a', encoding='utf-8') as trade_file:
        if how_much_str() == 0:
            trade_file.write(f'{value}')
        else:
            trade_file.write(f'\n{value}')


def how_much_str(file_name='bakery.csv'):
    with open(file_name, 'r', encoding='utf-8') as trade_file:
        return len(trade_file.readlines())


def show_sales(start=1, stop=how_much_str()):
    with open('bakery.csv', 'r', encoding='utf-8') as trade_file:
        str_number = 1
        for line in trade_file:
            if start <= str_number <= stop:
                print(line[:-1])
            str_number += 1
