# Задание 1

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 2))

# Задание 2 (Решил только с вашим объяснением, к сожалению)

raw_message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message = []
for element in raw_message:
    if element.isdigit():
        message.extend(['"', f'{int(element):02}', '"' ])
    elif element.startswith('+') or element.startswith('-') and element[1:].isdigit():
        message.extend(['"', f'{element [0]}{int(element[1:]):02}', '"'])
    else:
        message.append(element)
out_message = ' '.join(message)
print(out_message)

# Задание 4
names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for name in names:
    print('Здравствуйте, ' + name.split()[-1].capitalize())


# Задание 5
prices = [52.24, 567.34, 34.901, 456.987, 853.5, 21.1, 759.54, 52483.89921, 2.14, 4378.954]
print(id(prices))  #Узнаем id списка
prices.sort() #Сортировка по возрастанию
print(id(prices))  #Узнаем id отсортированного списка, чтобы сравнить с начальным id
for good in prices:
    rubs = int(good)
    cent = (good - rubs) * 100
    print(f'{rubs} рублей {cent:02.0f} копеек')
for good in prices[::-1]: #Сортировка по убыванию
    rubs = int(good)
    cent = (good - rubs) * 100
    print(f'{rubs} рублей {cent:02.0f} копеек')
for good in prices[::-1][:5]: #Сортировка по убыванию со срезом первых пяти, то есть, пяти наибольших
    rubs = int(good)
    cent = (good - rubs) * 100
    print(f'{rubs} рублей {cent:02.0f} копеек')