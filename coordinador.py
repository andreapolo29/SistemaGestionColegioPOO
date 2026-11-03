from persona import Persona

class Coordinador(Persona):
    def __init__(self, id, nombre, apellido, documento, telefono, correo, codigoCoordinador, area):
        super().__init__(id, nombre, apellido, documento, telefono, correo)
        self.codigoCoordinador = codigoCoordinador
        self.area = area

    def revisarSolicitud(self, solicitud):
        pass

    def aprobarTraslado(self, traslado):
        traslado.estado = "Aprobado"

    def asignarCurso(self, estudiante, curso):
        curso.agregarEstudiante(estudiante)