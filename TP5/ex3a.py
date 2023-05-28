#Definition des fonctions
def lectMat(n):
    A = []
    for i in range(n):
        Li = eval(input(f" ligne {i}: "))
        Li = list(Li)
        A.append(Li)
    return A

def affichMat(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]:>+.2f}\t", end =' ')
        print(f"|{A[i][n]:>+.2f}")

def Residu(A, b, x):
    n = len(A)
    res = 0.0
    for i in range(n):
        r = b[i]
        for j in range(n):
            r -= A[i][j] * x[j]
        res = max(res, abs(r))
    return res

def Jacobi(A, b, x, Kmax, tol):
    if tol <= 0:
        print('Tolérance trop petite')
        exit()
    n = len(A)
    x = list(x)
    ''' 
    while k < Kmax and Residu(A, b, x) >= tol:
        residue = Residu(A, b, x)
        for i in range(n):
            AX = 0
            if abs(A[i][i]) < 1e-16:
                raise ValueError('attention! pivot nul')
            else:
                for j in range(n):
                    if j != i:
                        AX += A[i][j] * x[j]
                x[i] = (b[i] - AX) / A[i][i]
        k += 1
    ''' 
    for k in range(Kmax):
        if (Residu(A, b, x) >= tol):
            residue = Residu(A, b, x)
            for i in range(n):
                AX = 0
                if abs(A[i][i]) < 1e-16:
                    raise ValueError('attention! pivot nul')
                else:
                    for j in range(n):
                        if j != i:
                            AX += A[i][j] * x[j]
                    x[i] = (b[i] - AX) / A[i][i]
        else:
            break

    print('solution approchée :')
    for i in range(n):
        print(f"{x[i]:>+.2f}\t", end =' ')
    print('le nombre d\'itérations :', k)
    print('le résidue :', residue)

#Execution du programme
n = int(input('Donner la taille du système : '))
print("Donnez la matrice augmentée : ")
A = lectMat(n)
tol = float(input('Donnez la tolérance : '))
x0 = eval(input('Donnez le vecteur initial x0 : '))
Kmax = int(input('Donnez Kmax : '))
b = [0] * n
for i in range(n):
    b[i] = A[i][n]

print("\nMatrice augmentée : ")
affichMat(A)

Jacobi(A, b, x0, Kmax, tol)
