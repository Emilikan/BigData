import math

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def main():
    file = pd.read_csv('./titanic.csv', escapechar='`', low_memory=False)

    main_data_frame = file[["Pclass", "Fare", "Age", "Sex", "Survived"]].dropna()  # очищаем от Nano(в)
    output = main_data_frame[["Pclass", "Fare", "Age", "Sex"]].replace("female", 0).replace("male", 1)
    clf = DecisionTreeClassifier(random_state=123)
    Y = main_data_frame['Survived']
    X = output

    print(X.columns)
    clf.fit(X, Y)
    print(clf.feature_importances_)
    print(clf.predict([[2, 80, 16, 1]]))


main()
