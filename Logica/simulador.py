import formatos_memoria
from Gestor import Gestor

import numpy as np

class Simulador:

    def __init__(self) -> None:
        self.memoria = np.zeros((int)((2**24)/4), dtype=int) #Tamaño total de memoria
        self.gestor = Gestor(self.memoria, 1)

    def initGestor(self, tipoGestor: int) -> None:
        self.memoria = np.zeros((int)((2**24)/4), dtype=int) #Tamaño total de memoria
        self.gestor = Gestor(self.memoria, tipoGestor)

    def getMemoria(self) -> list:
        return self.memoria

    def getGestorCreateProcess(self, nombre: str, tamaño: int) -> None:
        self.gestor.initProceso(nombre, tamaño)

    def getGestorRemoveProcess(self, PID: int, particion: int) -> None:
        self.gestor.removeProcess(PID, particion)
    
    def getGestorProcesos(self) -> list:
        return self.getGestorProcesos()

    def setAjuste(self, ajuste: int):
        if ajuste == 1:
            self.gestor.setMejorAjuste()
        elif ajuste == 2:
            self.gestor.setPeorAjuste()
        elif ajuste == 3:
            self.gestor.setPrimerAjuste()