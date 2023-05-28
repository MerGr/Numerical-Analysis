#question 1:
eps=1
count=0
while 1+eps>1:
    eps/=2
    count+=1
print('précision machine:',2*eps,eps)
print('count:',count)
#ce code calcule l'epsilon machine au 64bits, en divisant epsilon jusqu'à 1+eps=1, qui est 16 chiffres après la virgule
#Ca veut dire que eps a atteint une valeur telle que l'ordinateur le trouve négligeable (c-à-d équivalent à 0) contre 1
#2*eps est la plus petite valeur non équivalente au 0

#question 2:
a=1.
for i in range (1000) :
    a*=3
b=-a
c=a+b
print(a,b,c)
#a augmente exponentiellement au facteur de 3 jusqu'à atteindre le plafeau des valeurs valables 64bits
#et donc a prend la valeur d'infinie quand elle dépasse le plafeau, b prend -infinie et c la valeur non existante comme somme de inf et -inf
