# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Используйте генераторы или генераторные выражения.
# Сначала найдите способ определить уникальность элемента в списке. Подумайте о сохранении порядка исходного списка.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_num = (src[i] for i in range(0, len(src)) if src.count(src[i]) == 1)
result = list(unique_num)
print(result)
