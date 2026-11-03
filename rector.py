from persona import Persona

class Rector(Persona):
    def __init__(self, id, nombre, apellido, documento, telefono, correo, cargo):
        super().__init__(id, nombre, apellido, documento, telefono, correo)
        self.cargo = cargo

    def aprobarSolicitud(self, solicitud):
        solicitud.estado = "Aprobada"

    def consultarInformes(self):
        pass

    def gestionarColegio(self):
        pass