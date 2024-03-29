import numpy as np

def cross_entropy_error(y, t):
    if y.ndim == 1:     # y가 1차원이라면
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

        batch_size = y.shape[0]
        return -np.sum(t * np.log(y)) / batch_size



