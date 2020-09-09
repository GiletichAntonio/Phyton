# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

counter = 0
with open('text_file2.txt', "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        counter += 1
        line_words = line.split()
        print(line, 'Длинна строки: ', len(line_words))
    print('Всего строк в тексте: ', counter)

# with open('text_file2.txt', encoding="utf-8") as f:
#     my_line = f.readlines()
#     for index, value in enumerate(my_line, 1):
#         number_of_words = len(value.split())
#         print(f'Строка {index} содержит {number_of_words} слов')
