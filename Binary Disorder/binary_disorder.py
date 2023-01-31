from sklearn.metrics import confusion_matrix
import numpy as np

def binary_disorder():
    y_true = [int(x) for x in input().split()]
    y_pred = [int(x) for x in input().split()]

    cm = np.asarray(confusion_matrix(y_true,
                                    y_pred,
                                    labels=[1,0]),
                    dtype='float')

    cm_transpose = cm.T
    return print(cm_transpose)

binary_disorder()