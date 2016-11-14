import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2014)
# define portfolio
N = 5 # a number of assets
L = 4 # a number of days

# asset close prices
p = np.random.randint(10, 30, size=(N, 1)) + \
np.random.randn(N, 1) # a mixture of uniform and N(0,1) rvs

# print(p)
# print(p.shape)
# print()

r = np.random.randn(N, L)/50 # ~ N(0,1)
# print(r)
# print(r.shape)




for i in range(r.shape[0]):
    tmp = []
    for j in range(r.shape[1]):
        if(j == 0):
            tmp.append(p[i][0].tolist())
            y = p[i] * (1 + r[i][j])
        else:
            y = y * (1 + r[i][j])
            tmp.append(y.tolist()[0])

    if(i == 0):
        P = np.array(tmp)
    else:
        P = np.vstack([P, np.array(tmp)])
print(P)
print(P.shape)

# plt.figure(num=1, figsize=(8, 5))
# plt.plot(P.T, '+-')
# plt.xlabel("Days")
# plt.ylabel("Asset Close Price (\$)")
# plt.show()

m = np.mean(P, axis=1)
s = np.std(P, axis=1)

m = np.mean(P, axis=1) + np.zeros((N, L+1))
m = m.T
s = np.std(P, axis=1) + np.zeros((N, L+1))
s = s.T
normP = (P-m)/s

c = np.cov(normP)
print(c)
w, v = np.linalg.eig(c)

print(w)
print()