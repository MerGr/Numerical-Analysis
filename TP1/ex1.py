from numpy import int32

b=int32 (2**31 -1)
print(b)
print(int32(b+1))
print(int32(b+2))

#ce code donne la valeur de 2³¹-1, le plafeau des valeurs 32bits
#au mode 32 bits à b
#b+1 et b+2 dépasse le plafeau, on a un cas de overflow, et donc b+1 et b+2
#prend le minimum d'intervalle [-2³¹,2³¹-1] qui est -2³¹ et -2³¹+1 resp.
