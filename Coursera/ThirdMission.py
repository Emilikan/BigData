# машинное обучение, основанное на расстояноиях
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold


def main():
    file = pd.read_csv('./wine.data', escapechar='`', low_memory=False)
    x = file[['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
              'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'Diluted wines', 'Proline']]
    y = file['Class']

    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    print(kf)

    for train_index, test_index in kf.split(x):
        X_train, X_test = y[[train_index]], y[[test_index]]
        y_train, y_test = y[train_index], y[test_index]
    print("TRAIN:", X_train, "TEST:", )

    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(x, y)

    print(neigh.predict_proba([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))


main()
