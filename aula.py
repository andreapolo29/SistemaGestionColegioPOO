class Aula:
    def __init__(self, codigoAula, nombre, capacidad, tipo):
        self.codigoAula = codigoAula
        self.nombre = nombre
        self.capacidad = capacidad
        self.tipo = tipo
        self.disponible = True

    def consultarDisponibilidad(self):
        return self.disponible

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True