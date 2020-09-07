#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
elemCount = int(input("Введите количество элементов списка "))
itemsList = []
i = 0
el = 0
while i < elemCount:
    itemsList.append(input("Введите следующее значение списка "))
    i += 1


for elem in range(int(len(itemsList)/2)):
        itemsList[el], itemsList[el + 1] = itemsList [el + 1], itemsList[el]
        el += 2
print(itemsList)
