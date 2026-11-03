class Documento:
    def __init__(self, codigoDocumento, nombre, tipo):
        self.codigoDocumento = codigoDocumento
        self.nombre = nombre
        self.tipo = tipo
        self.estado = "Entregado"

    def cargar(self):
        pass

    def verificar(self):
        return True

    def actualizarEstado(self, estado):
        self.estado = estado