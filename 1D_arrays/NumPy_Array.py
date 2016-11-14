import numpy as np


a = np.array([1,2,3,4,5])
# b = a + 1
b=a.copy()
b=a+1
b[0]=7



print (a,b)
a.fill(0)
print(a)

# np.where
x=np.array([1,-2,3,4,-5])
i=np.where(x<0)

x.flat[i]=0
print(x)

r = np.array([0.09,-0.03,-0.04,0.07,0.00,-0.02])
rneg = r.clip(-1, 0)# ，-1以下的变成-1，0以上的变成0
print(rneg)



r2 = r.copy()
i = np.where(r2=0.)
print(r2[i])
rpos = r2.clip(0, 9)

