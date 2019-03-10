import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def main():
    file_train = pd.read_csv('./perceptron-train.csv', escapechar='`', low_memory=False)

    file_test = pd.read_csv('./perceptron-test.csv', escapechar='`', low_memory=False)

    X_train = file_train['x']
    Y_train = file_train[['y1', 'y2']]

    X_test = file_test['x']
    Y_test = file_test[['y1', 'y2']]

    clf = Perceptron(random_state=241, max_iter=5, tol=None)
    clf.fit(Y_train, X_train)
    new_arr = []
    for i in range(200):
        new_arr.append(clf.predict([[Y_test['y1'][i], Y_test['y2'][i]]])[0])

    print(accuracy_score(X_test, new_arr))

    return accuracy_score(X_test, new_arr)


def newSS():
    file_train = pd.read_csv('./perceptron-train.csv', escapechar='`', low_memory=False)

    file_test = pd.read_csv('./perceptron-test.csv', escapechar='`', low_memory=False)

    test_f_arr = []
    train_f_arr = []
    test_f_arr.append([-1.0, 1.6514365371, 1337.45382564])
    train_f_arr.append([-1.0, -0.0246259814315, 1174.60023796])
    for i in range(300):
        train_f_arr.append([file_train['x'][i], file_train['y1'][i], file_train['y2'][i]])
    for i in range(200):
        test_f_arr.append([file_test['x'][i], file_test['y1'][i], file_test['y2'][i]])
    print("g =", train_f_arr)
    scaler = StandardScaler()
    newV = scaler.fit_transform(train_f_arr)
    newT = scaler.transform(test_f_arr)

    X_v = []
    Y_v = []
    X_t = []
    Y_t = []
    for i in range(301):
        if i != 0:
            X_v.append(newV[i][0])
            Y_v.append([newV[i][1], newV[i][2]])

    for i in range(201):
        if i != 0:
            X_t.append(newT[i][0])
            Y_t.append([newT[i][1], newV[i][2]])

    clf = Perceptron(random_state=241, max_iter=5, tol=None)
    clf.fit(Y_v, file_train['x'])
    newtt = []
    for i in range(200):
        newtt.append(clf.predict([[Y_t[i][0], Y_t[i][1]]])[0])
    print(accuracy_score(file_test['x'], newtt))
    return accuracy_score(file_test['x'], newtt)


print("Otv =", newSS()-main())

