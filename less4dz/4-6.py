# 6. Реализовать два небольших скрипта: а) итератор, генерирующий целые числа, начиная с указанного, б) итератор,
# повторяющий элементы некоторого списка, определенного заранее. Подсказка: использовать функцию count() и cycle()
# модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть
# условие его завершения. Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
# прекращено.

from itertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el + 1)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "TypeError"

print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))
