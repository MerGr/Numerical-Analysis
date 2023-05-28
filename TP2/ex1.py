from math import cos,pi,log,ceil
import sys

e=sys.float_info.epsilon

def f(x):
    return (cos((pi*x)/4)-(x-0.5)**2)

def bissec(a,b,eps,Nmax):
    eps=10**(-eps)
    print("Le nombre d'itérations théorique est :",ceil(log((b-a)/eps)/log(2)))
    Nmax_init = Nmax
    while(abs(b-a)>=eps and Nmax != 0):
        c=(a+b)/2
        if f(c)==0 :
            break
        elif f(a)*f(c)<0:
            b=c
        else:
            a=c
        Nmax-=1
    r=c
    print("La racine est : " + '{:e}'.format(r) + "\nLe nombre d'itérations minimal est : " + str(Nmax_init-Nmax))
    if Nmax==0:
        print("Nombre Maximal d'itérations est atteint!")


a,b=eval(input("Donner l'intervalle : ")) 
a=int(a)
b=int(b)
eps=input("Donner la précision : ") 
eps=float(eps)
Nmax=input("Donner le nombre max d'itérations : ") 
Nmax=int(Nmax)
if f(a)*f(b)>0:
    print("Erreur. Pas de racine")
else:
    bissec(a,b,eps,Nmax)
