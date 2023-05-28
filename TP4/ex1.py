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
print('|     1 - Sans Kmax                                |')
print('|     2 - avec Kmax                                |')
print('####################################################')
option = input('Tapez votre option (1,2) :')
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
