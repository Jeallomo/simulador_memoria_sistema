import pandas as np
from numpy import empty

memoria = empty(2**24, dtype=bytes) #Tamaño total de memoria


x = 0

inicio = 1048576
fin = 1347890
numeroProceso = 45

# print("inicio")
# for a in arreglo:
#   if x >= inicio and x <= fin:
#     a = numeroProceso
#   x+=1

# particion fija (16MiB 32 particiones) = 524288 bytes
print(type(memoria))
