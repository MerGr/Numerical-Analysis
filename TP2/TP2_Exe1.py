# SMI4 GTP2 Poste 002 TP2_Exe1
# Graoui Abderrahmane
# Methode Point Fixe pour f(x) = x**2 - 4*sin(x) = 0
#----------------------------------------------------

from math import sin, sqrt

def PtsFix(g, x0, EPS, Nmax):
    cout = 0
    while abs(g(x0)-x0)>=EPS and cout < Nmax:
        r=g(x0)
        cout+=1
        if abs(r-x0)<EPS:
            break
        x0=r
    output=[cout, x0, abs(r-x0)]
    return output

def g1(x):
    return 2*sqrt(sin(x))

def g2(x):
    return 4*sin(x)/x



g=input("Le nom de la fonction : ")
g=eval(g)
while(g != g1 and g != g2 ):
    g=input("Le nom de la fonction : ")
    g=eval(g)

a,b=eval(input("Intervalle a,b : "))
while(b<=a):
    b = eval(input("Intervalle b superiere a a : "))

while((g(a)-a)*(g(b)-b) >= 0):
    a,b=eval(input("Intervalle a,b : "))
    while(b<=a):
        b = eval(input("Intervalle b superiere a a : "))

a=float(a)
b=float(b)
x0 = float(input("x0 = "))
while (x0 < a or x0 > b):
    x0 = input("x0 = ")

Nmax=int(input("Nmax = "))
while(Nmax <= 0):
    Nmax=input("Nmax = ")

EPS= float(input("EPS = "))

Res = PtsFix(g, x0, EPS, Nmax)

if Res[0] >= Nmax :
    print("ERREUR ! Nmax atteinte !")
else:
    print("n = ", '{:e}'.format(Res[0]))
    print("Xn = ", '{:e}'.format(Res[1]))
    print("Er = ", '{:e}'.format(Res[2]))