# Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield, полностью
# истощить генератор. Например:
# gen1 = iterator_without_yield(11)
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
# Без использования ключевого слова yield: генератор нечётных чисел от 1 до n (включительно), для чисел,
# квадрат которых меньше 200.

def iterator_without_yield(n):
    nums_gen = (num for num in range(1, n+1, 2))
    return nums_gen


gen1 = iterator_without_yield(11)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
