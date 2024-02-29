# SMI4 GTP2 Poste 002 TP1_Ex4a
# Graoui Abderrahmane
# TP1 Exercice 4 Question 3
#----------------------------------------------------
from math import log
import numpy as np
import matplotlib.pyplot as plt

def integral(n):
    return 1/(n+1) + log(11/10)
    
intgraph=[]
term=input('Value of n exponant for integral In: ')
term=int(term)
print('from 0 -------------------------->',term)
print('k\t|Integral')
print('==================================')
for i in range(0,int(term)+1):
    print(i,'\t|','{:e}'.format(integral(float(i))))
    intgraph.append('{:e}'.format(integral(float(i))))

plt.plot(intgraph)
plt.show()
