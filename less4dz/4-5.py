# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка. Подсказка: использовать функцию reduce().

from functools import reduce

print(reduce(lambda n, m: n * m, [y for y in range(100, 1001, 2)]))

# def mul_list(elem_1, elem_2):
#     return elem_1 * elem_2
#
# my_list = [elem for elem in range(100, 1001, 2)]
# print(f"Список\n{my_list}\nПроизведение чисел\n{reduce(mul_list, my_list)}")
#
