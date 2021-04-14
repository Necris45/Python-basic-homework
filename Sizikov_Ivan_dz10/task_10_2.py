# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать
# абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def material(self):
        pass


class Suit(Cloth):
    h = None

    def __init__(self, h):
        self.h = h

    @property
    def material(self):
        return 2 * self.h + 0.3


class Coat(Cloth):
    v = None

    def __init__(self, v):
        self.v = v

    @property
    def material(self):
        return self.v / 6.5 + 0.5


cloth_list = [Suit(2), Coat(18), Suit(4), Coat(20), Suit(5), Coat(15)]
total_material = 0
for cloth in cloth_list:
    total_material += cloth.material
print(f'{total_material:.2f}')
print(f'{cloth_list[0].material:.2f}')
print(f'{cloth_list[3].material:.2f}')
