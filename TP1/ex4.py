from math import log

def integral(n):
    if n==0.0:
        return log(11/10)
    else:
        return 1/n - 10*integral(n-1)

def inverse_integral(twon_integral,n):
    if twon_integral==log(11/10):
        return log(11/10)
    else:
        return (1/n - twon_integral)/10
    

term=input('Value of n exponant for integral In: ')
term=int(term)
print('from 0 -------------------------->',term)
print('k\t|Integral')
print('==================================')
for i in range(0,int(term)+1):
    print(i,'\t|','{:e}'.format(integral(float(i))))

twon_value=input('Value of '+ str(2*term) +' exponant integral: ')
twon_value=float(twon_value)
    
print('from',2*term,'-------------------------->',term)
print('k\t|Integral')
print('==================================')
print(2*int(term),'\t|',twon_value)
for i in range(2*int(term)-1,int(term)-1,-1):
    print(i,'\t|','{:e}'.format(inverse_integral(twon_value,i+1)))
    twon_value=inverse_integral(twon_value,i+1)
    
#Dans la première méthode, on calcule l'intégrale à l'aide de la machine, la machine donne la valeur + erreur machine non nul
#Quand la fonction du calcul s'éxecute récursivement, l'erreur machine s'augmente par facteur de 10 jusqu'à n=13 ou n=14 où dans ce cas on aura des
#valeurs plus et plus abhérrants, cependant dans la deuxième méthode, on donne déjà une valeur approximative d'intégrale 2n, l'erreur se divise en 10 approchant
#plus et plus au epsilon machine.
#En bref, la deuxième algorithme est plus stable que la première
