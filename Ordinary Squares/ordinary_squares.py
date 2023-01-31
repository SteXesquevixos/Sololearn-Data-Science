import numpy as np

def ordinary_squares():
    n, p = [int(x) for x in input().split()]

    X = []
    for i in range(n):
        X.append([float(x) for x in input().split()])

    y = [float(x) for x in input().split()]

    X = np.array(X)
    x_transpose = X.T
    x_inverse = np.linalg.inv((np.matmul(x_transpose, X)))

    beta = np.matmul((np.matmul(x_inverse, x_transpose)), np.array(y)).round(2)

    return print(beta)


ordinary_squares()