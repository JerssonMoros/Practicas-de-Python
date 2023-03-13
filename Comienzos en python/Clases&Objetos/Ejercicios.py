class Persona():
    def __init__(self, nombre, edad, dni) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f'Nombre: {self.nombre}, \n Edad: {self.edad}, \n DNI: {self.dni}')

    def esMayorDeEdad(self):
        return True if self.edad else False
