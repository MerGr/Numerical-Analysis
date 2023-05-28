#Definition des fonctions
def lectMat (n) :
    A = []
    for i in range (n):
        Li = eval(input (f" ligne : { i :} : "))
        Li = list(Li)
        A.append(Li)
    return (A)

def affichMat(A) :
    n = len(A)
    for i in range (n):
        for j in range (n):
            print(f"{A[i][j]:>+.2f}\t", end =' ')
        print(f"|{A[i][n]:>+.2f}")

def gaussElimin2(M) :
    n = len(M)
    for k in range(n-1):
        if abs(M[k][k]) < 1e-16:
            p = k+1
            if M[p][k] > 1e-16:
                for m in range (0,n+1):
                    M[p][m]+=M[k][m]
                    M[k][m]-=M[p][m]
                    M[p][m]-=M[k][m]
            else:
                p+=1
        for i in range(k+1, n):
            factor = M[i][k] / M[k][k]     
            for j in range(k, n+1):
                M[i][j] -= factor * M[k][j]

def Remontee(U):
    n = len(U)
    x = [0] * n
    for i in range(n-1, -1, -1):
        if abs(U[i][i]) < 1e-16:
            print("attention! pivot nul")
            exit()
        x[i] = U[i][n] / U[i][i]
        for j in range(i-1, -1, -1):
            U[j][n] -= U[j][i] * x[i]
            U[j][i] = 0
    return x
#Execution du Programme
n = input('Donner la taille du système : ')
n = int(n)
print("Donnez la matrice augmentée : ")
A = lectMat(n)
print("matrice avant élimination : ")
affichMat(A)
gaussElimin2(A)
print("matrice après élimination : ")
affichMat(A)
print("solution : ")
A = Remontee(A)
for i in range(n):
    print(f"{A[i]:>+.2f}\t", end =' ')
