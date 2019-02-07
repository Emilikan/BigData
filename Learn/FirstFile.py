import pandas as pd
import numpy as np
import pycountry
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from yandex_translate import YandexTranslate  # Используем класс YandexTranslate из модуля yandex_translate
from yandex_translate import YandexTranslateException

YANDEX_API_KEY = 'trnsl.1.1.20190204T194345Z.4133185b2e16c6ac.d41f764c3fae80785658cf1058b5d23a5557407f'
try:
    translate_obj = YandexTranslate(YANDEX_API_KEY)
except YandexTranslateException:
    translate_obj = None

# Размер надписей на графиках
PLOT_LABEL_FONT_SIZE = 14


# Генерация цветовой схемы
# Возвращает список цветов
def getColors11(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS


def translate1(string, translator_obj=None):
    if translator_obj is None:
        return string

    t = translator_obj.translate(string, 'en-ru')
    return t['text'][0]


translate = YandexTranslate('trnsl.1.1.20190204T194345Z.4133185b2e16c6ac.d41f764c3fae80785658cf1058b5d23a5557407f')
print('Languages:', translate.langs)
print('Translate directions:', translate.directions)
print('Detect language:', translate.detect('Как дела, Эмилька?'))
print('Translate:', translate.translate('Как дела, Эмилька?', 'en-ru')['text'][0])  # or just 'en'

df = pd.read_csv('./scrubbed.csv', escapechar='`', low_memory=False)
df = df.replace({'shape': None}, 'unknown')

country_label_count = pd.value_counts(df['country'].values)  # Получить из таблицы список всех меток country с их
# количеством
for label in list(country_label_count.keys()):
    c = pycountry.countries.get(alpha_2=str(label).upper())  # Перевести код страны в полное название
    # t = translate1(c.name, translate)  # Перевести название страны на русский язык
    # df = df.replace({'country': str(label)}, t)

shapes_label_count = pd.value_counts(df['shape'].values)
for label in list(shapes_label_count.keys()):
    t = translate1(str(label), translate_obj)  # Перевести название формы объекта на русский язык
    df = df.replace({'shape': str(label)}, t)

MONTH_COUNT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MONTH_LABEL = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

for i in df['datetime']:
    m, d, y_t = i.split('/')
    MONTH_COUNT[int(m) - 1] = MONTH_COUNT[int(m) - 1] + 1

MONTH_COUNT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MONTH_LABEL = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

for i in df['datetime']:
    m, d, y_t = i.split('/')
    MONTH_COUNT[int(m) - 1] = MONTH_COUNT[int(m) - 1] + 1

plt.bar(np.arange(12), MONTH_COUNT, color=getColors11(12))
plt.xticks(np.arange(12), MONTH_LABEL, rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Частота появления', fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.title('Частота появления объектов по месяцам', fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()

shapes_durations_dict = {}
for i in shapes_label_count:
    dfs = df[['duration (seconds)', 'shape']].loc[df['shape'] == i]
    shapes_durations_dict[i] = dfs['duration (seconds)'].mean(axis=0) / 60.0 / 60.0

shapes_durations_dict_keys = []
shapes_durations_dict_values = []

shapes_durations_dict[i] = dfs['duration (seconds)'].median(axis=0) / 60.0 / 60.0
OBJECT_COUNT = 5
for k in shapes_label_count:
    shapes_durations_dict_keys.append(k)
    shapes_durations_dict_values.append(shapes_durations_dict[k])
plt.title('Среднее время появление каждого объекта', fontsize=12)
plt.bar(np.arange(OBJECT_COUNT), shapes_durations_dict_values, color=getColors11(OBJECT_COUNT))
plt.xticks(np.arange(OBJECT_COUNT), shapes_durations_dict_keys, rotation=90, fontsize=16)
plt.ylabel('Среднее время появления в часах', fontsize=12)
plt.show()
