class Curso:
    def __init__(self, codigoCurso, nombre, grado, jornada, capacidad):
        self.codigoCurso = codigoCurso
        self.nombre = nombre
        self.grado = grado
        self.jornada = jornada
        self.capacidad = capacidad
        self.estudiantes = []

    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def retirarEstudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

    def asignarProfesor(self, profesor):
        pass

    def consultarEstudiantes(self):
        return len(self.estudiantes)