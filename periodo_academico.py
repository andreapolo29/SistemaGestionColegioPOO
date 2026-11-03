class PeriodoAcademico:
    def __init__(self, codigoPeriodo, nombre):
        self.codigoPeriodo = codigoPeriodo
        self.nombre = nombre
        self.estado = "Inactivo"

    def iniciarPeriodo(self):
        self.estado = "Activo"

    def cerrarPeriodo(self):
        self.estado = "Cerrado"

    def consultarEstado(self):
        return self.estado