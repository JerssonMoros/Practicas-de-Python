class User:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def saludo(self):
        print(f'Hola, te saluda {self.name} {self.last_name}')

class Administrator(User):

    def superSaludo(self):
        print(f'Hola, te saluda {self.name} y soy un administrador')
    

userAdmin = Administrator('JMoros','1')
userAdmin.saludo()
userAdmin.superSaludo()


# user = User('Jersson', 'Moros')
# print(user)

# user.saludo()

# user.name = 'Andres' # cambiar el valor de un atributo
# user.saludo() 

# del user.name # Setear un atributo
# user.saludo()

# del user # Eliminar un usurio
# print(user)

class Animal():
    def __init__(self, tipo, nombre, onomatopeya) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.onomatopeya = onomatopeya

    def saludo(self):
        print(f'Hola, mi nombre es {self.nombre}, soy un {self.tipo} y yo se {self.onomatopeya}')

gato = Animal(nombre='Michi', tipo='Gato', onomatopeya='maullar')
gato.saludo()

perro = Animal(nombre='Tamara', tipo='Perro', onomatopeya='ladrar')
perro.saludo()