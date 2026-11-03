class Solicitud:
    def __init__(self, codigoSolicitud, tipo, descripcion):
        self.codigoSolicitud = codigoSolicitud
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = "Pendiente"

    def crear(self):
        self.estado = "Creada"

    def cancelar(self):
        self.estado = "Cancelada"

    def cambiarEstado(self, estado):
        self.estado = estado

    def consultarEstado(self):
        return self.estado