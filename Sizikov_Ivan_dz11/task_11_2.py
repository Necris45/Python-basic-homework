# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyZeroDivizionError(ZeroDivisionError):
    pass


def my_div(x1, x2):
    try:
        x3 = x1 / x2
        return x3
    except ZeroDivisionError:
        raise MyZeroDivizionError


try:
    a = int(input("введите делимое "))
    b = int(input("введите делитель "))
    c = my_div(a, b)
    print(f"Результат деления {c}")
except MyZeroDivizionError:
    print('на ноль делить нельзя')
except ValueError:
    print("Нужно ввести число")
