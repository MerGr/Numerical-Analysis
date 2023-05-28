from math import sin, cos, pi, sqrt
def f(x):
    return -x/4 + sin(x/2) + pi/6 - sqrt(3)/2

def df(x):
    return -1/4 + cos(x/2)*1/2

def ddf(x):
    return -sin(x/2)*1/4

def newton(fonc,dfonc,x0,tol,nmax):
    count=0
    err=1
    print("n |Xn\t\t  |En\t\t |abs(En/En-1)\t|abs(En/En-1²)")
    print('-'*65)
    for i in range (nmax+1):
        count+=1
        r=x0-fonc(x0)/dfonc(x0)
        print(count,'|','{:e}'.format(x0),'|','{:e}'.format(abs(r-x0)),'|','{:e}'.format(abs((r-x0)/err)),'|','{:e}'.format(abs((r-x0)/err**2)))
        err=r-x0
        x0=r
        if(abs(err)<tol):
            break
    if(count>nmax):
        print("Suite divergente")
    else:
        print("La racine est:",'{:e}'.format(r),"Nombre d'itérations est:",count)
    print("Le facteur de convergence asymptotique est : ", '{:e}'.format(abs(ddf(x0)/df(x0))/2))
    print("La constante positive k :", '{:e}'.format(abs(df(x0))))

x0,tol,nmax=eval(input("Tapez la valeur initiale, la tolérance et nombre maximal d'itérations: "))
x0=float(x0)
tol=int(tol)
tol=10**(-tol)
nmax=int(nmax)
newton(f,df,x0,tol,nmax)

