# SMI4 GTP2 Poste 002 TP2_fonc1
# Graoui Abderrahmane
# Graphe pour TP2 Exercice 1
#----------------------------------------------------

from math import *

def g1(x):
    return 2*sqrt(sin(x))

def g2(x):
    return 4*sin(x)/x

#----------------------------------------------------

from matplotlib.pyplot import *
clf()
a = 1.; b = 3.; h = 0.01
x=[a]; y=[g1(a)]; z=[g2(a)]; N=floor((b-a)/h)

for i in range(1, N+1):
    x.append(x[0]+i*h)
    y.append(g1(x[i]))
    z.append(g2(x[i]))

plot(x,y,'b',label="y = g1(x)")
plot(x,z,'r',label="y = g2(x)")
plot([a,b],[a,b],'k',label="y = x")
legend(); title('Méthode du Point Fixe');
grid()
show()