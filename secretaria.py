from persona import Persona

class Secretaria(Persona):
    def __init__(self, id, nombre, apellido, documento, telefono, correo, codigoEmpleado, area):
        super().__init__(id, nombre, apellido, documento, telefono, correo)
        self.codigoEmpleado = codigoEmpleado
        self.area = area

    def registrarMatricula(self, matricula):
        matricula.registrar()

    def verificarDocumento(self, documento):
        return documento.verificar()

    def actualizarInformacion(self, estudiante):
        pass