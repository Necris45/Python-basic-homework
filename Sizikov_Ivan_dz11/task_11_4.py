# 4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f'{self.a} + {self.b}i'
        elif self.b < 0:
            return f'{self.a} - {abs(self.b)}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


x1 = Complex(3, 2)
print(x1)
x2 = Complex(2, -1)
print(x2)
y = x1 + x2
print(y)
z = x1 * x2
print(z)
