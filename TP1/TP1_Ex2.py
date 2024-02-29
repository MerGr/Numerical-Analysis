# SMI4 GTP2 Poste 002 TP1_Ex2
# Graoui Abderrahmane
# TP1 Exercice 2
#----------------------------------------------------
a=1.
for i in range (1000) :
    a*=3
b=-a
c=a+b
print(a,b,c)
#a augmente exponentiellement au facteur de 3 jusqu'à atteindre le plafeau des valeurs valables 64bits
#et donc a prend la valeur d'infinie quand elle dépasse le plafeau, b prend -infinie et c la valeur non existante comme somme de inf et -inf
