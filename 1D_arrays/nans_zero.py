import numpy as np

x = np.array([1, 2,0, np.nan, 3, 4,0, np.nan, 5])
i=x.nonzero()
print(type(i))
print(x[i])
# y=i[~np.isnan(x)].sum()
#
# print(y)