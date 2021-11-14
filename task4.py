"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, "go")

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn on', direction)

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        return 'speed exceeded' if super(TownCar, self).show_speed() > 60\
                else super(TownCar, self).show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, is_police=True)


town_car = TownCar(70, 'color', 'name', False)
police_car = PoliceCar(70, 'color', 'name')
print(police_car.is_police)
