from persona import Persona

class Estudiante(Persona):
    def __init__(self, id, nombre, apellido, documento, telefono, correo, codigoEstudiante, grado):
        super().__init__(id, nombre, apellido, documento, telefono, correo)
        self.codigoEstudiante = codigoEstudiante
        self.grado = grado
        self.estado = "Activo"

    def solicitarTraslado(self, destino):
        return destino

    def realizarSolicitud(self, tipo, descripcion):
        return tipo

    def consultarCalificaciones(self):
        pass

    def consultarHorario(self):
        pass