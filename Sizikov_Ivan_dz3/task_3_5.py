# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Усложнение: * Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import randrange


def get_jokes(n, is_not_repeatable=False):
    """
    Создает список шуток из рандомных слов из разных списков, с возможностью запретить повторный выбор слов
    :param is_not_repeatable: флаг, разрешающий(False) или запрещающий(True) повторно использовать элементы списка
    :param n: Кол-во шуток
    :return: выводит список шуток
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = list()
    # Проверяем возможность выдать требуемое кол-во шуток без повторов
    if is_not_repeatable and min(len(nouns), len(adverbs), len(adjectives)) < n:
        print(f'Сликом большое количество шуток, максимальное кол-во {min(len(nouns), len(adverbs), len(adjectives))}')
        return
    if is_not_repeatable:
        for i in range(0, n):
            rand_idx_nouns = randrange(len(nouns))
            rand_idx_adverbs = randrange(len(adverbs))
            rand_idx_adjectives = randrange(len(adjectives))
            jokes.append(f"{nouns[rand_idx_nouns]} {adverbs[rand_idx_adverbs]} {adjectives[rand_idx_adjectives]}")
            nouns.pop(rand_idx_nouns)
            adverbs.pop(rand_idx_adverbs)
            adjectives.pop(rand_idx_adjectives)
    else:
        for i in range(0, n):
            jokes.append(f"{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} "
                         f"{adjectives[randrange(len(adjectives))]}")
    print(jokes)


get_jokes(is_not_repeatable=True, n=3)
