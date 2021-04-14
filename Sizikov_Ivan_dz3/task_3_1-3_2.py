# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте: как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
# снаружи?

def num_translate(english_num):
    translate = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                 "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if english_num in translate:
        print(f'{translate[english_num]}')
    else:
        return None


# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(english_num):
    translate = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                 "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if english_num in translate:
        print(f'{translate[english_num]}')
    elif english_num.lower() in translate:
        if english_num.lower()[0] != english_num[0]:
            print(f'{translate[english_num.lower()].title()}')
        else:
            print(f'{translate[english_num.lower()]}')
    else:
        return None


num_translate_adv("one")
num_translate_adv("Two")
num_translate_adv("TeN")
