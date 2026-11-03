from persona import Persona

class PadreFamilia(Persona):
    def __init__(self, id, nombre, apellido, documento, telefono, correo, parentesco, ocupacion):
        super().__init__(id, nombre, apellido, documento, telefono, correo)
        self.parentesco = parentesco
        self.ocupacion = ocupacion

    def consultarInformacionEstudiante(self, estudiante):
        return estudiante.nombre

    def realizarSolicitud(self, tipo, descripcion):
        return tipo

    def consultarCalificaciones(self, estudiante):
        pass