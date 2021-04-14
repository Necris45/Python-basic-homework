# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.current_speed = 0
        self.direction = "Север"

    def go(self):
        print(f'Автомобиль {self.name} поехал')
        self.current_speed = self.speed

    def stop(self):
        print(f'Автомобиль {self.name} остановился')
        self.current_speed = 0

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль повернул на {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} составляет {self.current_speed}')


class TownCar(Car):
    def show_speed(self):
        if self.current_speed > 60:
            print(f'Скорость автомобиля {self.name} превысила допустимое значение в 60. '
                  f'Текущая скорость {self.current_speed}')
        else:
            print(f'Текущая скорость автомобиля {self.name} составляет {self.current_speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.current_speed > 40:
            print(f'Скорость автомобиля {self.name} превысила допустимое значение в 40. '
                  f'Текущая скорость {self.current_speed}')
        else:
            print(f'Текущая скорость автомобиля {self.name} составляет {self.current_speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


worker1 = WorkCar(50, "black", "Эвакуатор", False)
worker2 = WorkCar(30, "Blue", "Трактор", False)
town1 = TownCar(80, "White", "Mazda", False)
town2 = TownCar(58, "White", "Лада", False)
print(worker1.name, worker1.color, worker1.current_speed, worker1.direction, worker1.is_police)
worker1.go()
worker1.turn("юг")
worker1.show_speed()
worker1.stop()
worker1.show_speed()
print(worker2.name, worker2.color, worker2.current_speed, worker2.direction, worker2.is_police)
worker2.go()
worker2.turn("юг")
worker2.show_speed()
worker2.stop()
worker2.show_speed()
print(town1.name, town1.color, town1.current_speed, town1.direction, town1.is_police)
town1.go()
town1.turn("юг")
town1.show_speed()
town1.stop()
town1.show_speed()
print(town2.name, town2.color, town2.current_speed, town2.direction, town2.is_police)
town2.go()
town2.turn("юг")
town2.show_speed()
town2.stop()
town2.show_speed()
