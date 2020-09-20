# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_polise = is_police
        print(f"Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_polise}")

    def go(self):
        print(f'{self.name}: Машина поехала')

    def stop(self):
        print(f'{self.name} Машина остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {""}')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"Скорость автомобиля {self.speed}"


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Прпвышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Прпвышение скорости!' \
            if self.speed > 160 else f"{self.name}: Скорость автомобиля {self.speed}"


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('"Полицейский"', 'черный', 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Грузовик"', 'синий', 30)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

sport_car = SportCar('"Спортивный"', 'желтый', 130)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"Городская"', 'синий', 55)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'\nМашина {police_car.name} (цвет {police_car.color})')