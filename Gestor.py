from typing import List
import formatos_memoria
from proceso import Process

class Gestor:
    
    def __init__(self, memoria, formatoMemoria) -> None:
        self.memoria = memoria
        self.formatoMemoria = formatoMemoria
        self.particiones = formatos_memoria.getParticiones(self.formatoMemoria).copy()
        self.procesos = []

        #Formato de memoria:
        #   1: Estatica Fija
        #   2: Estatica Variable
        #   3: Dinamica sin Compactacion
        #   4: Dinamica con Compactacion

    def initProceso(self, nombre: str, tamaño: int) -> None:
        if self.formatoMemoria == 1:
            particionAsignada = self.getBaseEstaticaFija(tamaño)
            self.procesos.append(Process(len(self.procesos), particionAsignada, tamaño, nombre, 0))
            self.particiones
            print(self.procesos[len(self.procesos)-1].getPID())

    def getBaseEstaticaFija(self, tamaño: int) -> int:
        for part in self.particiones:
            if part[2] == False and (part[1] - part[0]) > tamaño:
                part[2] = True
                return (int)(part[0])
        return -1

    def getBaseEstaticaVariable(self) -> int:
        return 0

    def getBaseDinamicaSin(self) -> int:
        return 0

    def getBaseDinamicaCon(self) -> int:
        return 0

    