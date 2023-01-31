import numpy as np

def reshape_arr():
    r = int(input())

    lst = [float(x) for x in input().split()]
    arr = np.array(lst)

    array_2d = arr.reshape(r, int(len(lst) / r))

    return print(array_2d)

reshape_arr()