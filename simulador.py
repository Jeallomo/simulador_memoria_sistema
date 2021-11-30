import formatos_memoria
from Gestor import Gestor

import pandas as np
from numpy import empty


memoria = empty((int)((2**24)/4), dtype=int) #Tamaño total de memoria

gestor = Gestor(memoria, 1)
gestor.initProceso("Word", 50000)
gestor.initProceso("Chrome", 50000)
gestor.initProceso("Word", 50000)
gestor.initProceso("Chrome", 50000)

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
#print(gestor.getBaseEstaticaFija(500))
