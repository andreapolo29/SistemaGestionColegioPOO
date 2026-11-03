from persona import Persona

class Administrativo(Persona):
    def __init__(self, id, nombre, apellido, documento, telefono, correo, codigoEmpleado, cargo, area):
        super().__init__(id, nombre, apellido, documento, telefono, correo)
        self.codigoEmpleado = codigoEmpleado
        self.cargo = cargo
        self.area = area

    def consultarSolicitud(self, solicitud):
        return solicitud.estado

    def actualizarDatos(self):
        pass