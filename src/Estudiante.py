#crear una clase llamada estudiante que herede de la clase persona
#crear un metodo que imprima el nombre del estudiante
#crear un metodo que imprima la edad del estudiante
#crear un metodo que imprima el pais de origen del estudiante
#crear un metodo que imprima todos los datos del estudiante
#crear una instancia de la clase estudiante

from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, pais):
        super().__init__(nombre, edad, pais)
        
    def imprimir_nombre(self):
        print(self.nombre)
        
    def imprimir_edad(self):
        print(self.edad)
        
    def imprimir_pais(self):
        print(self.pais)
        
    def imprimir_datos(self):
        print(self.nombre, self.edad, self.pais)


