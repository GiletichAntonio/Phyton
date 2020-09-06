#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна,
#лето, осень).
#Напишите решения через list
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
user_month = int(input('input a number from 1 to 12: '))
if user_month in winter:
    print('Your month is winter')
elif user_month in spring:
    print('Your month is spring')
elif user_month in summer:
    print('Your month is summer')
elif user_month in fall:
    print('Your month is fall')
else:
    print('error')

#через dict.
months = {
    12: 'winter', 1: 'winter', 2:'winter',
    3: 'spring', 4: 'spring', 5:'spring',
    6: 'summer', 7: 'summer', 8:'summer',
    9: 'fall', 10: 'fall', 11:'fall',
}
user_month = int(input('input a number from 1 to 12: '))
print('your month is ', months[user_month])
