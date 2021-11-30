class Process:
    def __init__(self, PID: int, base:int, tamaño:int, nombre: str, estado:int) -> None:
        self.PID = PID
        self.base = base
        self.tamaño = tamaño
        self.nombre = nombre
        self.estado = estado

    def getPID(self) -> int:
        return self.PID
    
    def getBase(self) -> int:
        return self.base
    
    def getTamaño(self) -> int:
        return self.tamaño

    def getNombre(self) -> int:
        return self.nombre
    
    def getEstado(self) -> int:
        return self.estado