#crear una clase llamada curso
#crear un metodo que imprima el nombre del curso
#crear un metodo que imprima la duracion del curso
#crear una instancia de la clase curso
#crear un metodo que imprima todos los datos del curso


class Curso:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        
    def imprimir_nombre(self):
        print(self.nombre)
        
    def imprimir_duracion(self):
        print(self.duracion)
        
    def imprimir_datos(self):
        print(f"Nombre del curso: {self.nombre}, Duración: {self.duracion}")




