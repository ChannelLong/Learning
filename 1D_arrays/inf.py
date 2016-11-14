import numpy as np
def removeinf(x):
    i = np.where(x != np.inf)
    return x[i]
a = np.array([1.,2.,3.,4.,5.])
b = np.array([1.,2.,3.,0.,5.])
c = a/b
print(c)
try:
    np.asarray_chkfinite(c)#expected to return ValueError if inf has have been found in the array of c.
except ValueError:
    c = removeinf(c)
    print(c)


