class Colegio:
    def __init__(self, nombre, nit, direccion, telefono, correo):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.estudiantes = []

    def registrarSede(self, sede):
        pass

    def registrarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def consultarEstudiantes(self):
        for e in self.estudiantes:
            print(e.nombre)