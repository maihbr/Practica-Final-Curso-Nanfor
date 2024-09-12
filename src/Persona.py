#crear una clase persona que tenga como atributos nombre, edad y pais de origen
#crear un metodo que imprima el nombre de la persona
#crear un metodo que imprima la edad de la persona
#crear un metodo que imprima el pais de origen de la persona
#crear un metodo que imprima todos los datos de la persona
#crear una instancia de la clase persona

class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_edad(self):
        print(self.edad)

    def imprimir_pais(self):
        print(self.pais)

    def imprimir_datos(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, País: {self.pais}')
    


        