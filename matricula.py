class Matricula:
    def __init__(self, codigoMatricula):
        self.codigoMatricula = codigoMatricula
        self.estado = "Pendiente"

    def registrar(self):
        self.estado = "Registrada"

    def cancelar(self):
        self.estado = "Cancelada"

    def actualizarEstado(self, estado):
        self.estado = estado

    def verificarDocumentos(self):
        return True