from colegio import Colegio
from estudiante import Estudiante

def main():
    colegio = Colegio("Colegio UCC", "123", "Calle", "123", "correo@mail.com")
    estudiantes = []

    while True:
        print("1. Registrar Estudiante")
        print("2. Ver Estudiantes")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            documento = input("Documento: ")
            codigo = input("Código: ")
            grado = int(input("Grado: "))
            
            est = Estudiante(1, nombre, apellido, documento, "300", "mail@mail.com", codigo, grado)
            estudiantes.append(est)
            colegio.registrarEstudiante(est)
            print("Estudiante registrado con éxito")

        elif opcion == "2":
            colegio.consultarEstudiantes()

        elif opcion == "3":
            break

if __name__ == "__main__":
    main()