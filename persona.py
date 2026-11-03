class Persona:
    def __init__(self, id, nombre, apellido, documento, telefono, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.telefono = telefono
        self.correo = correo

    def iniciarSesion(self, correo, contraseña):
        return self.correo == correo

    def actualizarDatos(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo

    def consultarInformacion(self):
        return self.nombre