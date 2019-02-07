# файл примера функция для работы с .csv файлами и MySQL базами данных + пример работы с Api переводчика от яндекс +
# массивы

import pandas as pd
import sqlite3
import numpy as np

from yandex_translate import YandexTranslate  # Используем класс YandexTranslate из модуля yandex_translate


def traslater():
    translate = YandexTranslate(
        'trnsl.1.1.20190204T194345Z.4133185b2e16c6ac.d41f764c3fae80785658cf1058b5d23a5557407f')  # тут api

    print('Languages:', translate.langs)  # выводим все доступные языки
    print('Translate directions:', translate.directions)  # выводим языки, на которые можно переводить
    print('Detect language:', translate.detect('Как дела, Эмилька?'))  # определение языка
    print('Translate:', translate.translate('Как дела, Эмилька?',
                                            'ru-en'))  # Translate: {'code': 200, 'lang': 'ru-en',
    # 'text': ["What's# up, Emilka?"]}

    text = translate.translate("Приветик", 'ru-en')['text'][0]
    print(text)  # Greeting


def m_translate(string):
    # использовать эту функцию для перевода с англа на русский
    translate = YandexTranslate('trnsl.1.1.20190204T194345Z.4133185b2e16c6ac.d41f764c3fae80785658cf1058b5d23a5557407f')
    return translate.translate(string, 'en-ru')['text'][0]


def csv_pandas():
    file = pd.read_csv('./scrubbed.csv', escapechar='`', low_memory=False)  # выводим в переменную весь файл
    file.plot(figsize=(15, 10))  # это, вроде, должно создавать графики

    print(file[['datetime', 'comments']][:10])  # сразу два столбца 10 строк

    print(file['country'].value_counts())  # сколько встречается именно этого

    file = file['comments']
    is_nlo = file.str.contains('n')  # вывод True если 'n' есть в строке
    print(is_nlo[:4])

    # file.to_csv('data/weather_2012.csv')  # сохраняем данные в файл csv

    for i in file['datetime']:
        print(i)  # выводит все под datetime
        # вывод:
        # /2013 18:00
        # 11/30/2013 18:00
        # 11/30/2013 18:06

    for i in file['city']:
        print(i)  # выводим все из колонки "города"  (можем, например, применить переводчик)
        # вывод:
        # san
        # marcos
        # lackland
        # afb
        # chester(uk / england)


def sql_pandas():
    # так работать можно не только с SQL
    db = sqlite3.connect('./weather_2012.sqlite')
    file = pd.read_sql("SELECT * from weather_2012", db, index_col='id')  # index_col='id' добавляет колонку id
    print(file)  # печатаем весь файл

    # создаем новый файл и записываем в него данные из файла ./scrubbed.csv
    weather_df = pd.read_csv('./scrubbed.csv')
    con = sqlite3.connect("./test_db_new.sqlite")
    con.execute("DROP TABLE IF EXISTS weather_2012")  # SQL запрос
    weather_df.to_sql("weather_2012", con)
    con = sqlite3.connect("./test_db_new.sqlite")
    df = pd.read_sql("SELECT * from weather_2012", con)
    print(df)


def for_example(i, j):
    return 3 * i + j * 4


def m_numpy():
    # создание массивов:
    arr = np.array([1, 2, 3])  # создаем одномерный массив
    print(arr)
    print()

    arr2 = np.array([[1, 2, 5], [4, 5, 7]])  # создаем двумерный массив
    print(arr2)
    print()

    arr3 = np.zeros((3, 5))  # создаем массив из нулей размером 3 на 5
    print(arr3)
    print()

    arr4 = np.ones((2, 2, 2))  # создаем два массива размером 2x2 состоящий из едениц
    print(arr4)
    print()

    arr5 = np.eye(5)  # создаем единичную матрицу размером 5x5
    print(arr5)
    print()

    # действия:
    arr6 = np.arange(34, 200, 2)  # создаем массив от 34 до 200 с сшагом 2
    print(arr6)
    print()

    arr7 = np.fromfunction(for_example, (3, 4))  # применяем функцию ко всему массиву
    print(arr7)
    print()

    X = np.random.normal(loc=1, scale=10, size=(1000, 50))
    print(X)
