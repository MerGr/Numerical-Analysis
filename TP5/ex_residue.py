#définition des fonctions
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

n = int(input('Donner la taille du système : '))
print("Donnez la matrice augmentée : ")
A = lectMat(n)
tol = float(input('Donnez la tolérance : '))
x0 = eval(input('Donnez le vecteur initial x0 : '))
b = [0] * n
for i in range(n):
    b[i] = A[i][n]

print("\nMatrice augmentée : ")
affichMat(A)

print('Residue : ', Residu(A, b, x0))
