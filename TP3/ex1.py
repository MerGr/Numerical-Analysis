def f(x):
    return -x**3 +4*x-1

def DiffDiv(X,Y):
    D=Y
    n=len(X)-1
    for j in range(1,n+1):
        for i in range(n,j-1,-1):
            D[i]=(D[i]-D[i-1])/(X[i]-X[i-j])
    return D

X=[]
Y=[]
n=input('Saisir la taille des abscisses: ')
n= int(n)
for i in range (0,n):
    X.append(float(input('Saisir l\'abscisse N°'+str(i+1)+': ')))
    Y.append(float(input('Saisir l\'image N°'+str(i+1)+': ')))
    #Y.append(f(X[i]))
print('Les differences divisees sont: ',DiffDiv(X,Y))
