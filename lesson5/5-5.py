# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

sum_elem = 0
with open('text_f.txt', "w", encoding="utf-8") as my_file:
    for i in range(100):
        el = randint(1, 100)
        sum_elem += el
        my_file.write(str(el) + " ")

print(f"Сумма чисел в файле составит: {sum_elem}")
