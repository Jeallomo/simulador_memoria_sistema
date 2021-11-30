particionFija = ((int)(2**24)/16/4) #Tamaño de cada una de las particiones

estaticaFija = [
  [particionFija*0, particionFija*1, True],           #Particiones de 1MiB
  [(particionFija*1)+1, particionFija*2, True],
  [(particionFija*2)+1, particionFija*3, False],
  [(particionFija*3)+1, particionFija*4, False],
  [(particionFija*4)+1, particionFija*5, False],
  [(particionFija*5)+1, particionFija*6, False],
  [(particionFija*6)+1, particionFija*7, False],
  [(particionFija*7)+1, particionFija*8, False],
  [(particionFija*8)+1, particionFija*9, False],
  [(particionFija*9)+1, particionFija*10, False],
  [(particionFija*10)+1, particionFija*11, False],
  [(particionFija*11)+1, particionFija*12, False],
  [(particionFija*12)+1, particionFija*13, False],
  [(particionFija*13)+1, particionFija*14, False],
  [(particionFija*14)+1, particionFija*15, False],
  [(particionFija*15)+1, particionFija*16, False]
]

estaticaVariable = [
  [particionFija*0, particionFija*1, False],             #1MiB
  [(particionFija*1)+1, particionFija*5, False],         #4MiB
  [(particionFija*5)+1, particionFija*7, False],         #2Mib         
  [(particionFija*7)+1, particionFija*9, False],         #2Mib
  [(particionFija*9)+1, particionFija*10, False],        #1Mib
  [(particionFija*10)+1, particionFija*11, False],       #1Mib
  [(particionFija*11)+1, particionFija*12, False],       #1Mib
  [(particionFija*12)+1, particionFija*13, False],       #1Mib
  [(particionFija*13)+1, particionFija*13.5, False],     #0.5Mib
  [(particionFija*13.5)+1, particionFija*14, False],     #0.5Mib
  [(particionFija*14)+1, particionFija*14.5, False],     #0.5Mib
  [(particionFija*14.5)+1, particionFija*15, False],     #0.5Mib
  [(particionFija*15)+1, particionFija*15.25, False],    #0.25Mib
  [(particionFija*15.25)+1, particionFija*15.5, False],  #0.25Mib
  [(particionFija*15.5)+1, particionFija*15.75, False],  #0.25Mib
  [(particionFija*15.75)+1, particionFija*16, False]     #0.25Mib
]

dinamica = []     #Ingresar objetos de la siguiente forma [posicion_inicio, posicion_final, true/false (si esta ocupado)] cuando es sin compactacion

def getParticiones(type: int) -> list:
  if type == 1:
    return estaticaFija
  elif type == 2:
    return estaticaVariable
  else:
    return dinamica