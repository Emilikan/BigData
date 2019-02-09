import math

import pandas as pd
import numpy as np
from collections import Counter


def number_one():
    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False)
    summ = file['Sex'].value_counts()[1]
    print(file['Sex'].value_counts()[0])
    print(summ)


def number_two():
    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False)
    surv = file['Survived'].value_counts()[1]
    all = file['Survived'].value_counts()[1] + file['Survived'].value_counts()[0]
    print(surv / all * 100)


def number_three():
    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False)
    first_class = file['Pclass'].value_counts()[1]
    all = file['Survived'].value_counts()[1] + file['Survived'].value_counts()[0]
    print(first_class / all * 100)


def number_four():
    na_values = ['NO CLUE', 'N/A', '0', 'nan', 'NaN']
    file = pd.read_csv('./titanic.csv', na_values=na_values, escapechar='`', low_memory=False)
    summ = 0
    counter = 0
    a = list()

    for i in file['Age']:
        if not math.isnan(i):
            summ += i
            counter += 1
            a.append(i)

    print(summ/counter)

    if counter % 2 == 0:
        a = sorted(a)
        print(a[int(counter/2)])
    else:
        print(summ/2)



def number_five():
    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False, dtype={'Age': str})

    # кореляция
    print(file['SibSp'].corr(file['Parch']))





def number_six():
    # ответ не верный

    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False, dtype={'Age': str})
    m_file = file['Name']
    is_Missis = m_file.str.contains('s.')
    is_Miss = m_file.str.contains('Miss.')

    names = list()
    counter = 0
    for i in is_Missis:
        is_to = False

        if i:
            if is_Miss[counter]:
                is_t = False
                new_str = ''
                stre = file['Name'][counter]
                is_first_probel = True

                for ik in stre:
                    if ik == '.':
                        is_t = True
                    elif ik == ' ':
                        if is_t:
                           is_to = True

                    if is_to:
                        if ik != ' ':
                            new_str += ik
                        elif is_first_probel:
                            is_first_probel = False
                        else:
                            is_to = False
                names.append(new_str)
            else:
                stre = file['Name'][counter]
                new_str = ''
                is_t = False
                is_first_probel = True
                for ik in stre:
                    if ik == '(':
                        is_t = True
                    elif ik == ' ':
                        if is_t:
                            is_to = True

                    if is_to:
                        if ik != ' ':
                            new_str += ik
                        elif is_first_probel:
                            is_first_probel = False
                        else:
                            is_to = False
                names.append(new_str)

        counter += 1
    print(names)


number_five()
