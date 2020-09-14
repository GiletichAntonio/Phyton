# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    def __init__(self, title="Что-то, что может рисовать"):
        self.title = title

    def draw(self):
        print(f"Давайте начнем рисовать! {self.title}!!!")


class Pen(Stationery):
    def draw(self):
        print(f"Начнем рисовать {self.title} ручкой.")


class Pencil(Stationery):
    def draw(self):
        print(f"Начнем рисовать {self.title} карандашом.")


class Handle(Stationery):
    def draw(self):
        print(f"Начнем рисовать {self.title} маркером.")


stat = Stationery()
stat.draw()
pen = Pen("Монбланк")
pen.draw()
pencil = Pencil("Паркер")
pencil.draw()
handle = Handle("Брауберг")
handle.draw()