# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете
# ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
def type_logger(func):
    def logger(*args, **kwargs):
        log_string = f'{func.__name__}'
        for arg in args:
            log_string += f'({arg}: {type(arg)}), '  # Позволит использовать для функций с большим кол-вом аргументов
        print(log_string[:-2])                      # после составления строки позволит удалить лишний пробел и запятую
        function_result = func(*args, **kwargs)
        return function_result
    return logger


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
