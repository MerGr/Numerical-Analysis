from math import *
def E1(value):
    return (1-cos(value))/sin(value)**2

def E2(value):
    return 1/(1+cos(value))

print('|x\t\t\t|E1\t\t\t|E2\t\t\t\t')
print('--------------------------------------------------------------------')
for i in range(11):
    x=10**-i
    print('|','{:e}'.format(x),'\t\t|','{:e}'.format(E1(x)),'\t\t|','{:e}'.format(E2(x)))
