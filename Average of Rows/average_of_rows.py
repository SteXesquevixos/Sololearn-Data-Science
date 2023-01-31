import numpy as np

def rowmeans():
    n, p = [int(x) for x in input().split()]

    input_values = []
    for i in range(n):
        input_values.append(input().split())

    arr = np.array(input_values).astype(np.float16)
    values = np.mean(arr[:, :], axis=1).round(2)

    return print(f'{values}')

rowmeans()