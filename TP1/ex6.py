def trinome(a,b,c):
    delta=b**2-4*a*c
    if delta > 0:
        racine1 = (b-delta**1/2)/2*a
        racine2 = (b+delta**1/2)/2*a
        print('Les racines sont : r1='+str(racine1)+' r2='+str(racine2))
    elif delta < 0:
        return 'pas de racines'
    else:
        racine = b/2*a
        print('La racine est : r='+str(racine))

x,y,z=eval(input('Enter value of a,b and c respectively : '))
trinome(x,y,z)


#la valeur 2**-600*2 atteint la valeur de epsilon machine, donc
#delta=2**-600*2 - 4*1*0 = 0 pour la machine même si mathématiquement
#2**-600*2 n'est pas nul
#d'où on obtient la racine (2**-600)/2 = 2**-601
