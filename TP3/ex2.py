from math import cos,pi

def f(x):
    return -x**3 +4*x-1

def g(x):
    return (0.5*x + 2)*cos(pi*x)

def h(x):
    return 1/(1+x**2)

def Horner(X,Y,t):
    p=Y[len(Y)-1]
    for i in range(len(Y)-2,-1,-1):
        p=Y[i]+(t-X[i])*p
    return p

def Eg(x,P):
    return abs(g(x) - P)

def DiffDiv(X,Y):
    D=Y
    n=len(X)-1
    for j in range(1,n+1):
        for i in range(n,j-1,-1):
            D[i]=(D[i]-D[i-1])/(X[i]-X[i-j])
    return D

def equidistErreur(a,b,n,F):
    Y=[]
    X=[]
    maxErr = 0
    for i in range (0,501):
        X.append(a+i*(b-a)/501)
    for i in range (0,501):
        Y.append(F(X[i]))
    for i in range(0,n+1):
        Pn=Horner(X,DiffDiv(X,Y),X[i])
        r=abs(F(X[i]-Pn))
        if(maxErr < r):
            maxErr = r
    return maxErr

#Execution du programme
print('#############################################')
print('# Choisir quelles fonction à calculer       #')
print('# 1- f(x) = -x³ + 4*x -1                    #')
print('# 2- g(x) = (0.5 * x +2)*cos(pi*x)          #')
print('# 3- h(x) = 1/(1+x²)                        #')
print('# 4- Images à saisir                        #')
print('#############################################')
usr_choice = 0
while(usr_choice != 1 and usr_choice != 2 and usr_choice !=3 and usr_choice != 4):
    usr_choice = input('Choisir votre option (1,2,3,4): ')
    usr_choice=int(usr_choice)

#Execution du choix
if(usr_choice == 1):
    X=eval(input("Saisir les abscisses: "))
    Y=[]
    for i in range (0,len(X)):
        Y.append(f(X[i]))
    print('Les differences divisees sont: ',DiffDiv(X,Y))
    interpolValue=input('Saisir la valeur à interpoler: ')
    interpolValue=float(interpolValue)
    print('P('+str(interpolValue)+')=',Horner(X,DiffDiv(X,Y),interpolValue))

    
if(usr_choice == 2):
    bornes= eval(input('Introduire les bornes : '))
    deg = int(input('Donner le degré : '))
    t = bornes[0] -1

    while(t<bornes[0] or t>bornes[1]):
        t=input('Donner le point t dans ['+str(bornes[0])+','+str(bornes[1])+']: ')
        t=float(t)
    Y=[]
    X=[]
    for i in range (0,deg+1):
        X.append(bornes[0]+i*(bornes[1]-bornes[0])/deg)
    for i in range (0,deg+1):
        Y.append(g(X[i]))
    Pn=Horner(X,DiffDiv(X,Y),t)
    print('La valeur du polynome en '+str(t)+' est: ',Pn)
    print('L\'Erreur commise en '+str(t)+' est : ',Eg(t,Pn))
    print('Erreur équidistants : ',equidistErreur(bornes[0],bornes[1],deg,g))


if(usr_choice == 3):
    bornes= eval(input('Introduire les bornes : '))
    deg = int(input('Donner le degré : '))
    print('Erreur équidistants : ',equidistErreur(bornes[0],bornes[1],deg,h))
    
if(usr_choice == 4):
    X=eval(input("Saisir les abscisses: "))
    Y=eval(input("Saisir les images: "))
    print('Les differences divisees sont: ',DiffDiv(X,Y))
    interpolValue=input('Saisir la valeur à interpoler: ')
    interpolValue=float(interpolValue)
    print('P('+str(interpolValue)+')=',Horner(X,DiffDiv(X,Y),interpolValue))

