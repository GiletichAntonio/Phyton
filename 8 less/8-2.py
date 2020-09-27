# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class DivideOnZero:
    def __init__(self, divisor, dividend):
        self.divisor = divisor
        self.dividend = dividend

    @staticmethod
    def divide_on_zero(divisor, dividend):
        try:
            return divisor / dividend
        except:
            return f"Деление на ноль недопустимо"


div = DivideOnZero(22, 222)
print(int(DivideOnZero.divide_on_zero(234, 1)))
print(DivideOnZero.divide_on_zero(10, 0.1234))
print(div.divide_on_zero(234, 0))
