def miFuncion(): #Funcion normal
    print('Hola Mundo')

miFuncion()

def saludandome(miNombre): #funcion enviando variable como parametro
    print(f'Hola {miNombre}')

saludandome('Jersson')

def saludandome2(miNombre, miApellido): # Funcion enviado dos variables como aprametro
    print(f'Hola {miNombre} {miApellido}')

saludandome2('Jersson', 'Garzon') 

def saludandome3(miApellido, miNombre): # Funcion enviando variables definidas como parametro
    print(f'Hola {miNombre} {miApellido}')

saludandome3(miNombre='Jersson Andres', miApellido='Garzon Moros')

def saludandome4(*args): # Funcion enviado multiples variables en un solo parametro (Se devuelve una tupla)
    for arg in args:
        print(f'Hola {arg}')

saludandome4('Jersson', 'Andres', 'Garzon', 'Moros')

def saludandome5(**kwargs): # Funcion enviando variables y se convierte en diccionario
    print('Hola', kwargs['miNombre'], '-', kwargs['miApellido'])

saludandome5(miApellido = 'Moros', miNombre = 'Andres')

def saludo(person = 'Todos'): #Funcion con variable definida por defecto
    print(f'Hola {person}')

saludo('Jersson')