# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield. Полностью истощить
# генератор. Например:
# gen1 = iterator_with_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
# Усложнение(*):
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), для чисел,
# квадрат которых меньше 200.

def iterator_with_yield(n):
    for num in range(1, n + 1, 2):
        yield num


gen1 = iterator_with_yield(11)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
