from math import cos,sin,sqrt,log,ceil

def g1(x):
    return 2*sqrt(sin(x))

def g2(x):
    return 4*sin(x)/x

def g1_prime(x):
    return -cos(x)/sqrt(sin(x))

def g2_prime(x):
    return (4*cos(x)*x-4*sin(x))/(x**2)

def ptFixe(x0,EPS,Nmax):
    niter=0
    r=0
    k=g1_prime(x0)
    while abs(g1(x0)-x0)>=EPS and niter<=Nmax:
        #print("DEBUG : Iteration "+str(niter)+": x="+str(x0)+" |g(x)="+str(r))
        r=g1(x0)
        x0=r
        niter+=1
        if(abs(g1_prime(x0))>k):
            k=abs(g1_prime(x0))
    print("La constante positive k :",'{:e}'.format(k))
    if(niter>Nmax):
        return 'Méthode divergente'
    else:
        return 'La racine approx. est : '+ '{:e}'.format(r) ,"Le nombre d'itérations minimale est : " + str(niter)
    

x0,EPS,Nmax=eval(input("Donnez valeur initiale, précision et nombre d'itérations : "))
x0=float(x0)
EPS=float(EPS)
EPS=10**(-EPS)
Nmax=int(Nmax)
L=abs(g1_prime(x0))+0.000001
L=float(L)
print("Nombre d'itérations théorique:",ceil(abs(log(abs((1-L)*EPS))-log(abs(g1(x0)-x0)))/log(L)))
print(str(ptFixe(x0,EPS,Nmax)))

#Commentaire:
#Quelque soit la valeur initiale, g2 revient erreur 'méthode divergente', cependant g1 converge vers la racine.
