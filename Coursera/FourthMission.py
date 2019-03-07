import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler


def main():
    file_train = pd.read_csv('./perceptron-train.csv', escapechar='`', low_memory=False)

    file_test = pd.read_csv('./perceptron-test.csv', escapechar='`', low_memory=False)

    X_train = file_train['x']
    Y_train = file_train[['y1', 'y2']]

    X_test = file_test['x']
    Y_test = file_test[['y1', 'y2']]

    clf = Perceptron(random_state=241)
    clf.fit(Y_train, X_train)
    print(clf.predict([[0.10406073501, -2050.21767738]]))

main()