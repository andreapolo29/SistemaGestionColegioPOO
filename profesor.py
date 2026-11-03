from persona import Persona

class Profesor(Persona):
    def __init__(self, id, nombre, apellido, documento, telefono, correo, codigoProfesor, especialidad):
        super().__init__(id, nombre, apellido, documento, telefono, correo)
        self.codigoProfesor = codigoProfesor
        self.especialidad = especialidad

    def asignarCalificacion(self, estudiante, nota):
        pass

    def consultarHorario(self):
        pass

    def registrarAsistencia(self, estudiante):
        pass