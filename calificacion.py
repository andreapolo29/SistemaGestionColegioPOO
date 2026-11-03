class Calificacion:
    def __init__(self, idCalificacion, nota, observacion):
        self.idCalificacion = idCalificacion
        self.nota = nota
        self.observacion = observacion

    def registrarNota(self, nota):
        self.nota = nota

    def actualizarNota(self, nota):
        self.nota = nota

    def consultarNota(self):
        return self.nota