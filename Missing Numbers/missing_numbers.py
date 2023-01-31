import numpy as np
import pandas as pd

def missing_numbers():
    lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]

    series = pd.Series(lst)
    null_values = series.isnull()

    for i in range(len(null_values)):
        if null_values[i] == True:
            series.iloc[i] = series.mean().round(1)

    return print(series)

missing_numbers()