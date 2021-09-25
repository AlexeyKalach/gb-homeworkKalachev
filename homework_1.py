# Задание 1
duration = int(input('Введите время в секундах: '))
days = duration // (60*60*24)  # кол-во дней
hours = (duration - days * (60 * 60 * 24)) // (60 * 60)  # кол-во часов
minutes = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60  # кол-во минут
seconds = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60  # кол-во секунд
if days > 0:
    print(days, 'дни', hours, 'часы', minutes, 'минуты', seconds, 'секунды')
elif hours > 0:
    print(hours, 'часы', minutes, 'минуты', seconds, 'секунды')
elif minutes > 0:
    print(minutes, 'минуты', seconds, 'секунды')
else:
    print(seconds, 'секунды')


# Задание 2 (c)
cubes = []
for number in range(1, 1001, 2):  # Перебираем первую тысячу чисел
    cubes.append(number ** 3)
final_sum = 0
for number in cubes:
    number += 17
    current_sum = 0
    for current_number in str(number):
        current_sum += int(current_number)
        if current_sum % 7 == 0:
            final_sum += number
print(final_sum)

# Задание 3 (Не справился с 100, решил с 20, как у вас)
percent = int(input('Введите число процента: '))
if percent == 1:
    percent_word = 'процент'
elif percent <= 4:
    percent_word = 'процента'
else:
    percent_word = 'процентов'
print(percent, percent_word)