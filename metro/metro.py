import numpy as np

# В качестве основы для модели была взята схема московского метрополитена.
# Для простоты рассматриваются лишь несколько линий.
# Для хранения информации о станциях линии используются списки.
# Цифра в названиии станции указывает на принадлежность к линии.
# Также задается список crosses с парами станций, между которыми есть переход.

line_1 = ['1Бульвар Рокоссовского', '1Черкизовская', '1Преображенская площадь', '1Сокольники', '1Красносельская',
          '1Комсомольская', '1Красные ворота', '1Чистые пруды', '1Лубянка', '1Охотный ряд', '1Библиотека им. Ленина',
          '1Кропоткинская', '1Парк культуры', '1Фрунзенская', '1Спортивная', '1Воробьевы горы', '1Университет',
          '1Проспект Вернадского', '1Юго-Западная', '1Тропарево']

line_2 = ['2Алма-Атинская', '2Красногвардейская', '2Домодедовская', '2Орехово', '2Царицыно', '2Кантемировская',
          '2Каширская', '2Коломенская', '2Автозаводская', '2Павелецкая', '2Новокузнецкая', '2Театральная', '2Тверская',
          '2Маяковская', '2Белорусская', '2Динамо', '2Аэропорт', '2Сокол', '2Войковская', '2Водный стадион',
          '2Речной вокзал']

line_3 = ['3Пятницкое шоссе', '3Митино', '3Волоколамская', '3Мякинино', 'Строгино', '3Крылатское', '3Молодежная',
          '3Кунцевская', '3Славянский бульвар', '3Парк Победы', '3Киевская', '3Смоленская', '3Арбатская',
          '3Площадь Революции', '3Курская', '3Бауманская', '3Электрозаводская', '3Семеновская', '3Партизанская',
          '3Измайловская', '3Первомайская', '3Щелковская']

line_5 = ['5Белорусская', '5Новослободская', '5Проспект Мира', '5Комсомольская', '5Курская', '5Таганская',
          '5Павелецкая', '5Добрынинская', '5Октябрьская', '5Парк культуры', '5Киевская', '5Краснопресненская']

crosses = [['1Комсомольская', '5Комсомольская'], ['1Охотный ряд', '2Театральная', '3Площадь Революции'],
           ['1Библиотека им. Ленина', '3Арбатская'], ['1Парк культуры', '5Парк культуры'],
           ['2Белорусская', '5Белорусская'], ['2Павелецкая', '5Павелецкая'], ['3Курская', '5Курская'],
           ['3Киевская', '5Киевская']]

all_stations = [line_1, line_2, line_3, line_5]

# Ниже представлен алгоритм ввода станций отправки и назначения. Их названия сохраняются в переменные а и b.
# Если введенной станции нет среди представленных в модели, программа выдает ошибку.
# Если в модели присутствуют несколько станций с введенным названием, предлагается уточнить линию метро.

a = input('Введите станцию отправки: ')
matches = []
n = 0
for i in np.concatenate((line_1, line_2, line_3, line_5)):
    if i[1:] == a:
        matches.append(i)
if len(matches) == 0:
    print('Ошибка: станция не найдена')
    raise SystemExit
elif len(matches) > 1:
    n = input(f'Найдено {len(matches)} станций с названием {a}(На линиях {matches[0][:1]} и {matches[1][:1]}). '
        f'\nПожалуйста, уточните номер линии: ')
    if n != matches[0][:1] and n != matches[1][:1]:
        print('Ошибка: станция не найдена')
    else:
        matches.clear()
        matches.append(n + a)
a = matches[0]

b = input('Введите станцию назначения: ')
matches.clear()
n = 0
for i in np.concatenate((line_1, line_2, line_3, line_5)):
    if i[1:] == b:
        matches.append(i)
if len(matches) == 0:
    print('Ошибка: станция не найдена')
    raise SystemExit
elif len(matches) > 1:
    n = input(f'Найдено {len(matches)} станций с названием {b}(На линиях {matches[0][:1]} и {matches[1][:1]}). '
          f'\nПожалуйста, уточните номер линии: ')
    if n != matches[0][:1] and n != matches[1][:1]:
        print('Ошибка: станция не найдена')
    else:
        matches.clear()
        matches.append(n + b)
b = matches[0]

print(f"\nПеречень станций между станциями {a[1:]} линии {a[:1]} и {b[1:]} линии {b[:1]}: ")

# Ниже представлен алгоритм для случая, когда а и b находятся на одной линии:
if a[:1] == b[:1]:
    for i in all_stations:
        if a in i:
            for j in range(i.index(a), i.index(b), -1 if i.index(a) > i.index(b) else 1):
                if b != i[j] != a:
                    print(i[j][1:])
# Ниже представлен алгоритм для случая, когда на пути между а и b требуется пересадка.
# Если линии пересекаются в нескольких местах, выбирает кратчайший путь.
else:
    matches.clear()
    for i in crosses:
        if a[:1] in map(lambda x: x[:1], i) and b[:1] in map(lambda x: x[:1], i):
            matches.append(i)
    if len(matches) > 1:
        distance = [[], []]
        for i in matches:
            for line in all_stations:
                if a in line:
                    for j in i:
                        if a[:1] in j[:1]:
                            distance[matches.index(i)].append(abs(line.index(a) - line.index(j)))
        for i in matches:
            for line in all_stations:
                if b in line:
                    for j in i:
                        if b[:1] in j[:1]:
                            distance[matches.index(i)].append(abs(line.index(b) - line.index(j)))
        matches = matches[distance.index(min(distance))]
    match_lines = list(map(lambda x: x[:1], matches))
    for i in all_stations:
        if a in i:
            for j in range(i.index(a), i.index(matches[match_lines.index(a[:1])]), -1 if i.index(a) > i.index(matches[match_lines.index(a[:1])]) else 1):
                if matches[match_lines.index(a[:1])] != i[j] != a:
                    print(i[j][1:])
            print(matches[match_lines.index(a[:1])][1:])
    print(f'Пересадка со станции {matches[match_lines.index(a[:1])][1:]} линии {a[:1]} '
          f'на станцию {matches[match_lines.index(b[:1])][1:]} линии {b[:1]}')
    for i in all_stations:
        if b in i:
            print(matches[match_lines.index(b[:1])][1:])
            for j in range(i.index(matches[match_lines.index(b[:1])]), i.index(b), -1 if i.index(b) < i.index(matches[match_lines.index(b[:1])]) else 1):
                if b != i[j] != matches[match_lines.index(b[:1])]:
                    print(i[j][1:])


