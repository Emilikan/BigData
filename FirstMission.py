import pandas as pd


def number_one():
    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False)
    summ = file['Sex'].value_counts()[0] + file['Sex'].value_counts()[1]
    print(summ)


def number_two():
    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False)
    surv = file['Survived'].value_counts()[1]
    all = file['Survived'].value_counts()[1] + file['Survived'].value_counts()[0]
    print(surv/all * 100)

number_two()