class Traslado:
    def __init__(self, codigoTraslado, motivo, destino):
        self.codigoTraslado = codigoTraslado
        self.motivo = motivo
        self.destino = destino
        self.estado = "Pendiente"

    def solicitar(self):
        self.estado = "Solicitado"

    def aprobar(self):
        self.estado = "Aprobado"

    def rechazar(self, motivo):
        self.estado = "Rechazado"

    def consultarEstado(self):
        return self.estado