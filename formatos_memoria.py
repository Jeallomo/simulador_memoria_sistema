particionFija = ((2**24)/16) #Tamaño de cada una de las particiones

divisiones_de_memoria = [
  [particionFija*0, particionFija*1],
  [(particionFija*1)+1, particionFija*2],
  [(particionFija*2)+1, particionFija*3],
  [(particionFija*3)+1, particionFija*4],
  [(particionFija*4)+1, particionFija*5],
  [(particionFija*5)+1, particionFija*6],
  [(particionFija*6)+1, particionFija*7],
  [(particionFija*7)+1, particionFija*8],
  [(particionFija*8)+1, particionFija*9],
  [(particionFija*9)+1, particionFija*10],
  [(particionFija*10)+1, particionFija*11],
  [(particionFija*11)+1, particionFija*12],
  [(particionFija*12)+1, particionFija*13],
  [(particionFija*13)+1, particionFija*14],
  [(particionFija*14)+1, particionFija*15],
  [(particionFija*15)+1, particionFija*16]
]