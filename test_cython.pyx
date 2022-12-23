# https://blog.paperspace.com/boosting-python-scripts-cython/
# https://medium.com/towards-data-science/numpy-array-processing-with-cython-1250x-faster-a80f8b3caa52

import time
import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def do_calc(np.ndarray[np.double_t, ndim=1] arr):
    cdef int max_val
    cdef double total
    cdef int k
    cdef double t1, t2, t
    cdef int arr_shape = arr.shape[0]

    t1 = time.time()

    for k in range(arr_shape):
        total = total + arr[k]

    print "Total = ", total

    t2 = time.time()
    t = t2 - t1
    print("%.20f" % t)