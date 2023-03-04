birth_day = int(input("Введите день рождения: "))
month = input("Введите месяц рождения: ")
if month == 'december':
    astro_sign = 'Стрелец' if (birth_day < 22) else 'козерог'
elif month == 'january':
    astro_sign = 'козерог' if (birth_day < 20) else 'Водолей'
elif month == 'february':
    astro_sign = 'Водолей' if (birth_day < 19) else 'Рыбы'
elif month == 'march':
    astro_sign = 'Рыбы' if (birth_day < 21) else 'овен'
elif month == 'april':
    astro_sign = 'Овен' if (birth_day < 20) else 'телец'
elif month == 'may':
    astro_sign = 'Телец' if (birth_day < 21) else 'близнецы'
elif month == 'june':
    astro_sign = 'Близнецы' if (birth_day < 21) else 'рак'
elif month == 'july':
    astro_sign = 'Рак' if (birth_day < 23) else 'лев'
elif month == 'august':
    astro_sign = 'Лев' if (birth_day < 23) else 'дева'
elif month == 'september':
    astro_sign = 'Дева' if (birth_day < 23) else 'весы'
elif month == 'october':
    astro_sign = 'Весы' if (birth_day < 23) else 'скорпион'
elif month == 'november':
    astro_sign = 'скорпион' if (birth_day < 22) else 'стрелец'
print("Ваш знак зодиака:", astro_sign)
