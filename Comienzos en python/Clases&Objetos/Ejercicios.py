class Persona():
    def __init__(self, nombre, edad, dni) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        datos = 'Nombre: {}, \n Edad: {}, \n DNI: {}'
        print(datos.format(self.nombre, self.edad, self.dni))

    def esMayorDeEdad(self):
        return True if self.edad else False
