# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    day = 0
    month = 0
    year = 0

    @classmethod
    def convert(cls, date):
        temp_list = date.split("-")
        try:
            Data.day = int(temp_list[0])
            Data.month = int(temp_list[1])
            Data.year = int(temp_list[2])
        except ValueError:
            Data.day = 0
            Data.month = 0
            Data.year = 0

    @staticmethod
    def is_correct(date):
        Data.convert(date)
        if 1 <= Data.day <= 31 and 1 <= Data.month <= 12:
            return True
        else:
            return False

    def __init__(self, date):
        if Data.is_correct(date):
            self.date = date
        elif Data.day < 1:
            print('введенные данные не соответствуют требованиям, нужно было ввести строку формата «день-месяц-год»')
        else:
            print("Введены неверные данные, одно из значений слишком большое")


x = Data('йц-01-2010')
y = Data('12-45-2010')
z = Data('12-02-2015')
print(z.date)
