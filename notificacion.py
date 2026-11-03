class Notificacion:
    def __init__(self, codigoNotificacion, mensaje):
        self.codigoNotificacion = codigoNotificacion
        self.mensaje = mensaje
        self.estado = "No leída"

    def enviar(self):
        self.estado = "Enviada"

    def marcarLeida(self):
        self.estado = "Leída"

    def consultarNotificacion(self):
        return self.mensaje