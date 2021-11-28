class Process:
    def __init__(self, PID: int, base:int, tamano:int, nombre: str, estado:int) -> None:
        self.PID = PID
        self.base = base
        self.tamano = tamano
        self.nombre = nombre
        self.estado = estado