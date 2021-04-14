# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить
# исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Уточнение
# Текст до собаки (Local-part): латинские буквы, цифры и символы: ' . _ + -
#
# Текст после собаки (Domain part): латинские буквы, цифры и символы . -
#
# В Domain part обязательно должна быть хотя бы одна точка.
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли
# смысл в данном случае использовать функцию re.compile()?
import re

validator = re.compile(r"([a-z0-9]+[\.\+'_-])*[a-z0-9]+@[a-z0-9]+([\.-][a-z0-9]+)*\.[a-z]{2,6}",
                       flags=re.IGNORECASE)


def email_parse(email):
    result = validator.match(email)
    if result is None:
        msg = f' wrong email: {email}'
        raise ValueError(msg)
    else:
        data_list = email.split("@")
        return {'username': data_list[0], 'domain': data_list[1]}


x = email_parse("someone@geek.brains.ru")
print(x)
