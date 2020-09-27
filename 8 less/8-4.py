# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class WareHouse:

    def __init__(self, model_name, department, reg_num, count_num):
        self.model_name = model_name
        self.department = department
        self.reg_num = reg_num
        self.count_num = count_num

    def __str__(self):
        return f"Название модели: {self.model_name}, Отдел: {self.department}, " \
               f"Рег. номер: {self.reg_num}, Кол-во: {self.count_num} "


class Printer(WareHouse):
    pass


class Scanner(WareHouse):
    pass


class Xerox(WareHouse):
    pass


printer_1 = Printer('Pantum P2200 Series', 'Менеджер 1', 2342342, 4)
scanner_1 = Scanner('Canon MG8100 series Printer WS', 'Бухгалтерия', 3245342, 1)
xerox_1 = Xerox('brother dcp-l2500dr', 'РОП', 15678756, 3)
print('{0}\n{1}\n{2}'.format(printer_1, xerox_1, scanner_1))
