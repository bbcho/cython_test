from .cython_test import do_calc
import numpy as np

arr = np.arange(100_000, dtype=np.double)
print(do_calc(arr))
a = "test"