from math import cos,sin,sqrt,log,ceil
import sys

e=sys.float_info.epsilon
def f(x):
    return x**3

def f_prime(x):
    return 3*x**2

def g(x):
    return -x**3

def g_prime(x):
    return -3*x**2

def ptfixe(a,b,x0,EPS,Nmax):
    count=0
    for i in range (Nmax+1):
        if (x0 < a or x0 > b):
            return 'Hors intervalle'
        count+=1
        r=f(x0)
        #print("DEBUG: r=",r,"|x0=",x0, "|EPS=",EPS, "|r-x0=",r-x0)
        if(abs(r-x0))<EPS:
            #print(e)
            return 'Le point fixe: '+str(r)+"\nNombre d'itérations est: "+str(count)
        x0=r
    if count > Nmax:
        return 'Limite atteinte'

a,b,x0,EPS,Nmax=eval(input("Donnez l'intérvalle, valeur initiale, précision et nombre d'itérations : "))
a=float(a)
b=float(b)
x0=float(x0)
EPS=float(EPS)
EPS=10**(-EPS)
Nmax=int(Nmax)
L=abs(f_prime(x0))
L=float(L)
print("Nombre d'itérations théorique:",ceil((log(abs((1-L)*EPS))-log(abs(f(x0)-x0)))/log(L)))
print("La constante positive k :",'{:e}'.format(L))
print(str(ptfixe(a,b,x0,EPS,Nmax)))
