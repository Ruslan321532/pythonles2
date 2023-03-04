# Логический тип данных, условные конструкции и операторы.
# bool - boolean (логический тип данных)
# print(type(False))

# a = 10
# a = a + 8
# a += 9
# print(a)


'''логический оператор'''
# and, or, not
# print(not True)

'''Операторы сравнения'''
# print(2 == 3)
# print(2 != 3)
# print(2 > 3)
# print(2 < 3)
# print(2 <= 3)
# print(2 >= 3)
# print(2 > 1 or 2 == 3)
# print(2 > 1 and 2 == 3)
# print(1 < 2 > 3)


'''написать программу световора'''


# word = 'Qwe123aSd$@'
# print(not word.isalnum())

# print(len(word))
# print(word.isnumeric())
# print(word.isalpha())

# password = input('enter password: ')
#
# if len(password) >= 8 and len(password) <= 18:
#     print('длина подходит')
#     if not password.isalnum():
#         print('пароль надежный!')
#     else:
#         print('пароль ne надежный!')
# else:
#     print('длина ne подходит')


temperature = int(input('enter degree: '))
#
if temperature >= -40 and temperature <= 10:
    print('холодно')
elif temperature >= 11 and temperature <= 20:
    print('прохладно')
elif temperature >= 21 and temperature <= 27:
    print('тепло')
elif temperature >= 28 and temperature <= 52:
    print('жарко')
else:
    print('Че за погода, ваа!')

# age = int(input('enter age: '))
# limit = 18
#
# if age >= limit:
#     print('welcome')
# else:
#     print(f'возраст не подходит! come back after {limit - age} year')

# signal = 'green'

# if signal == 'green':
#     print('go')
# elif signal == 'yellow':
#     print('wait')
# elif signal == 'ref':
#     print('stop')
# else:
#     print('look at situation')


# time = 'morning'
#
# if time == 'morning':
#     print('good morning')
# elif time == 'day':
#     print('good afternoon')
# elif time == 'evening':
#     print('good evening')
# else:
#     print('Hello')
