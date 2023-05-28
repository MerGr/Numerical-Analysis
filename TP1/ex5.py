def somme(n):
    return 1/(n**4)

def somme1(n):
    sum_value=0
    for i in range(1,n+1):
        sum_value+=somme(i)
    return sum_value

def somme2(n):
    sum_value=0
    for i in range(n,0,-1):
        sum_value+=somme(i)
    return sum_value

term=1
while term !=0 :
    term=input('input n value : ')
    term=int(term)
    print('Somme 1 = ' + str(somme1(term)))
    print('Somme 2 = ' + str(somme2(term)))


#L'erreur machine dans la somme 1 se diminue par facteur de 1/€⁴, alors il va tendre vers epsilon machine
#Cependant pour la somme 2, l'erreur machine augmente par facteur de 1/€⁴,
#alors à terme n, la valeur 1/(1+epsilon_machine) pour la somme 1 est 1/(1+€⁴**n) pour la somme 2
