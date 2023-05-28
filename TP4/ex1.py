from math import log 

#Définition des fonctions
def Trapeze(a,b,N,g):
    h = (b-a)/N
    i = 1
    Tn = g(a) + g(b)
    while(i<N):
        Tn += 2*g(a+i*h)
        i+=1
    return Tn * h/2

def Milieu(a,b,N,g):
    h = (b-a)/N
    i = 0
    Mliu = 0
    while(i<N):
        Mliu += g((a+i*h + a+(i+1)*h)/2)
        i += 1
    return h*Mliu

def Simpson(a,b,m,g):
    h = (b-a)/(2*m)
    i = 1
    j = 0
    Spsn = g(a) + g(b)
    while(i < m):
        Spsn += 2*g(a+2*i*h)
        i += 1
    while(j < m):
        Spsn += 4*g(a+(2*j+1)*h)
        j += 1
    return h/3 * Spsn

def Ordre(G1,G2,m):
    return log(G1/G2)/log(1-1/m)
    
    
def f(x):
    return log(1+x)

def F(x):
    return log(1+x)*(1+x)-x

def Er(g,G):
    return abs(G-g)

def Rap(Er,g,G):
    return Er(g*2,G)/Er(g,G)


    
#Execution du programme
bornes=eval(input('Donnez les bornes : '))
I=F(bornes[1])-F(bornes[0])
print('Integrale exacte =','{:.6e}'.format(I))
print('####################################################')
print('| Choisir votre option :                           |')
print('|  -> Trapèze :                                    |')
print('|     1 - Sans Kmax                                |')
print('|     2 - avec Kmax                                |')
print('|  3- Point Milieu                                 |')
print('|  4- Simpson                                      |')
print('####################################################')
option = input('Tapez votre option (1,2,3,4) :')
if(option == '1'):
    N=0
    while(N < 1):
         N=int(input('Donnez le nombre de subdivision : '))
         if(N < 1):
             print('Erreur, il faut que N >= 1')
    Tn = Trapeze(bornes[0],bornes[1],N,f)
    print('Integrale Approchee =','{:.6e}'.format(Tn))
    print('Erreur commise =','{:.6e}'.format(Er(Tn,I)))
if(option == '2'):
    k = 1
    Kmax =int(input('Donnez Kmax: '))
    EPS = float(input('Donnez EPS: '))
    Tn = Trapeze(bornes[0],bornes[1],2**k,f)
    print('N|h\t\t|Tn(f)\t\t|Rh(f)\t\t|Rap\t')
    print('------------------------------------------------------------------------------')
    while(Er(Tn,I) >= EPS and k < Kmax):
         Tn = Trapeze(bornes[0],bornes[1],2**k,f)
         h = (bornes[1]-bornes[0])/2**k
         print(2**k,'|','{:e}'.format(h),'|','{:e}'.format(Tn),'|','{:e}'.format(Er(Tn,I)),'|','{:e}'.format(Rap(Er,Tn,I)))
         k += 1
if(option == '3'):
    N=0
    while(N < 1):
         N=int(input('Donnez le nombre de subdivision : '))
         if(N < 1):
             print('Erreur, il faut que N >= 1')
    Tn = Milieu(bornes[0],bornes[1],N,f)
    print('Integrale Approchee =','{:.6e}'.format(Tn))
    print('Erreur commise =','{:.6e}'.format(Er(Tn,I)))
if(option == '4'):
    N=0
    i=1
    while(N < 1):
         N=int(input('Donnez le nombre de subdivision : '))
         if(N < 1):
             print('Erreur, il faut que N >= 1')
    Tn = Simpson(bornes[0],bornes[1],N,f)
    Tn_minus = 0
    print('Integrale Approchee =','{:.6e}'.format(Tn))
    print('Erreur commise =','{:.6e}'.format(Er(Tn,I)))
    EPS = float(input('Donnez EPS: '))
    print('m|h\t\t|Sm(f)\t\t|Rm(f)\t\t|K\t')
    print('------------------------------------------------------------------------------')
    while(Er(Tn,I) >= EPS and i <= N ):
         Tn = Simpson(bornes[0],bornes[1],i,f)
         if(i>1):
             Tn_minus = Simpson(bornes[0],bornes[1],i-1,f)
         h = (bornes[1]-bornes[0])/(2*i)
         print(i,'|','{:e}'.format(h),'|','{:e}'.format(Tn),'|','{:e}'.format(Er(Tn,I)),'|','{:e}'.format(Ordre(Er(Tn,I),Er(Tn_minus,I),N)))
         i += 1

