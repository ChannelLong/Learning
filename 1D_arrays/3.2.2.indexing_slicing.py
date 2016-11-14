#Basic Use of Boolean Arrays
import numpy as np
x = np.array([1.0, 3. , 2.6, 4.3, 7.7, 5.6])
y = np.array([1. , 2.6, 3., 4. , 7. , 5.6])

cmp=(x==y)
# print(cmp)
#
# if(cmp.sum()==len(x)):
#     print('the same')
# else:
#     print('different')


i = 0
if(cmp.all()):
    print("All elements are the same")
elif(cmp.any()):
    print("Some elements are the same, i.e.:")

    for e in cmp:
        if(e):# tests if e==True (a useful trick!)
            print('%.1f'%x[i])
        i+=1
    print('---')

    for e in x:
        j=np.where(e==y)# 数列e与y的哪里相同 a tuple containing arrays with indexes
        print(j)
        if (j[0].size!=0):
             print(y[j])
else:
    print('all elements are different')

