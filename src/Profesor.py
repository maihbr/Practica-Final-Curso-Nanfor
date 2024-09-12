
#crear una clase llamada profesor que herede de la clase persona
#crear un metodo que imprima el nombre del profesor
#crear un metodo que imprima la edad del profesor
#crear un metodo que imprima el pais de origen del profesor
#crear un metodo que imprima todos los datos del profesor
#crear una instancia de la clase profesor

# Importar la clase Persona
from Persona import Persona

class Profesor(Persona):
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




















