# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = ''
        self.strings = len(list_of_lists)
        self.columns = len(max(list_of_lists, key=len))
        for i in range(0, self.strings):
            self.matrix += '|\t'
            for j in range(0, self.columns):
                if j < len(list_of_lists[i]):
                    self.matrix += f'{list_of_lists[i][j]}\t'
                else:
                    self.matrix += f'0\t'
            self.matrix += '|\n'


x = Matrix([[3, 5, 9, 15], [1, 4, 6], [8, 5, -7, 25]])
print(x.matrix)
