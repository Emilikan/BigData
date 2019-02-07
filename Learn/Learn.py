def condition(a):
    if a % 2 == 0:
        return "четное"
    elif a % 3 == 0:
        return "дел-ся на 3"
    else:
        return "ничего"


def strings():
    a = 'Привет'
    b = "Как дела?"
    print('''Привет
    
    да, можно так
    я сам в шоке''')

    # через пробел
    print(a, b)

    # друг за другом
    print(a + b)

    # на разных строках
    print(a)
    print(b)

    # или
    print(a + '\n' + b)

    genome = 'Emilka'
    print(genome[0])  # E
    print(genome[-1])  # a

    genome[1] = 'c'  # ошибка!!


def string_methods():
    a = 'пРИвет'
    p = 'Эмилька'

    # верхний - нижний регистр:
    a.upper()  # 'ПРИВЕТ'
    a.lower()  # 'привет'
    a.count(p)  # сколько раз встречается строка p в строку a
    a.find(p)  # позиция первого вхождения p в строке a (если -1, то не входит)
    newStr = a.replace('п', 'Now')  # заменяет все 'п' на 'Now', причем a не меняется


def cycles(a):
    while a < 0:
        a -= 1
        if a % 2 == 0:
            print(a + "четное")

    for i in 2, 3, 5:
        print(i * i)
        # 4 9 25

    for i in range(10):
        print(i * i)
        # 0 1 4 9 16 ... 81

    for i in range(2, 15, 4):
        print(i)
        # все числа от 2 до 15 (не включая 15) с шагом 4
        # левая граница всегда включая, правая - не вклюачаю


def m_list():
    students = ['Ivan', 'Emil', 'Oleg']
    for st in students:
        print('Hello, ' + st + '!')

    print(students[0])  # Ivan
    len(students)  # длинна списка

    students[2] = 'Marina'  # так изменять можно
    students.append('Olga')  # добавление в конец списка
    students += ['Boris', 'Sergey']  # добавление одного списка в конец другого
    students.insert(1, 'R')  # вставка элемента на определенный индекс в списке (остальные элементы сдвигаются)

    students.remove('Oleg')  # удаление значение (первое вхождение)
    del students[0]  # удаление по индексу

    # поиск
    if 'Emil' in students:
        print('Ivan is here')

    id = students.index('Emil')  # вернет индекс найденного элемента (или ошибку)
    
