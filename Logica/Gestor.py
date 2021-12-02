from typing import List
import formatos_memoria
from proceso import Process

class Gestor:
    
    def __init__(self, memoria, formatoMemoria) -> None:
        self.memoria = memoria
        self.formatoMemoria = formatoMemoria
        self.ajuste = 1
        self.particiones = formatos_memoria.getParticiones(self.formatoMemoria).copy()
        self.procesos = []
        self.count = 1

        #Formato de memoria:
        #   1: Estatica Fija
        #   2: Estatica Variable
        #   3: Dinamica sin Compactacion
        #   4: Dinamica con Compactacion

    def initProceso(self, nombre: str, tamaño: int) -> None:
        if self.formatoMemoria == 1:
            particionAsignada = self.getBaseEstaticaFija((int)(tamaño/4))
            self.procesos.append(Process(self.count, particionAsignada[0], tamaño, nombre, 0, particionAsignada[1]))
            proceso = self.procesos[len(self.procesos)-1]
            self.fillMemoria(proceso.getBase(), proceso.getBase() + (int)(proceso.getTamaño()/4), proceso.getPID())
            self.count += 1

    def getBaseEstaticaFija(self, tamaño: int) -> list:
        for part in self.particiones:
            if part[2] == False and (part[1] - part[0]) > tamaño:
                part[2] = True
                return [(int)(part[0]), self.particiones.index(part)]
        return [-1,-1]

    def getBaseEstaticaVariable(self, tamaño: int) -> int:
        particion = 0       

        if self.ajuste == 1:
            diferencia = self.particiones[0][1] - self.particiones[0][0]
            for x in range(1,len(self.particiones)):
                if (self.particiones[x][1] - self.particiones[x][0]) < diferencia and self.particiones[x][2] == False:
                    diferencia = self.particiones[x][1] - self.particiones[x][0]
                    particion = x
            if particion != 0:
                return [self.particiones[particion][0], particion]
            else:
                return [-1,-1]
        elif self.ajuste == 2:
            diferencia = self.particiones[0][1] - self.particiones[0][0]
            for x in range(1,len(self.particiones)):
                if (self.particiones[x][1] - self.particiones[x][0]) > diferencia and self.particiones[x][2] == False:
                    diferencia = self.particiones[x][1] - self.particiones[x][0]
                    particion = x
            if particion != 0:
                return [self.particiones[particion][0], particion]
            else:
                return [-1,-1]
        elif self.ajuste == 3:
            for x in range(1,len(self.particiones)):
                if (self.particiones[x][1] - self.particiones[x][0]) > tamaño and self.particiones[x][2] == False:
                    return [self.particiones[x][0], x]
        return [-1,-1]

    def getBaseDinamicaSin(self) -> int:
        return 0

    def getBaseDinamicaCon(self) -> int:
        return 0

    def setMejorAjuste(self) -> None:
        self.ajuste = 1
    
    def setPeorAjuste(self) -> None:
        self.ajuste = 2
    
    def setPrimerAjuste(self) -> None:
        self.ajuste = 3

    def fillMemoria(self, inicio: int, fin: int, PID: int) -> None:
        for direccion in range(inicio, fin+1):
            self.memoria[direccion] = PID

    def removeProcess(self, PID: int, particion: int) -> None:
        if self.formatoMemoria != 4:
            self.particiones[particion][2] = False          #Identifica a la particion como libre
            for x in range(len(self.procesos)):       #Remueve al proceso de la lista de procesos
                if self.procesos[x].getPID() == PID:
                    self.procesos.pop(x)
            for x in range(self.particiones[particion][0],self.particiones[particion][1]+1):  #Libera el espacio en la memoria
                self.memoria = 0
        else:
            self.compactMemoria(particion)
            for x in range(len(self.procesos)):       #Remueve al proceso de la lista de procesos
                if self.procesos[x].getPID() == PID:
                    self.procesos.pop(x)
        return

    def compactMemoria(self, particion: int) -> None:
        backup = self.memoria[self.particiones[particion][0]:self.particiones[particion][1]+1].copy()
        del self.memoria[self.particiones[particion][0]:self.particiones[particion][1]+1]
        self.memoria += backup.copy()

        if particion < (len(self.particiones)-1):
            for x in range(particion+1,len(self.particiones)):
                self.particiones[x][0] -= len(backup)
                self.particiones[x][1] -= len(backup)

        del self.particiones[particion]
    
    def getProcesos(self) -> list:
        return self.procesos