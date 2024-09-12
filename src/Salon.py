#crear un metodo que imprima el nombre del salon
#crear un metodo que imprima el grupo del salon
#crear un metodo que imprima el curso del salon
#crear un metodo que imprima el profesor del salon
#crear un metodo que imprima los estudiantes del salon
#crear una instancia de la clase salon

class Salon:
    def __init__(self, nombre, grupo, curso, profesor, estudiantes):
        self.nombre = nombre
        self.grupo = grupo
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes
        
    def imprimir_nombre(self):
        print(f"Nombre: {self.nombre}")
        
    def imprimir_grupo(self):
        print(f"Grupo:\n\t  {self.grupo.nombre}")
        
    def imprimir_curso(self):
        print(f"Curso:\n\t Nombre: {self.curso.nombre}, Duración: {self.curso.duracion}")
        
    def imprimir_profesor(self):
        print(f"Profesor:\n\t Nombre: {self.profesor.nombre}, Edad:  {self.profesor.edad}, País:{self.profesor.pais}")
        
    def imprimir_estudiantes(self):
        print("Estudiantes del salon:")
        for estudiante in self.estudiantes:
            print(f"\tNombre: {estudiante.nombre}, Edad: {estudiante.edad},País: {estudiante.pais}")
    

