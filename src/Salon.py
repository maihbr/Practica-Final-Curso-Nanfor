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
        print(f"Nombre del salon: {self.nombre}")
        
    def imprimir_grupo(self):
        print(f"Grupo del salon: {self.grupo}")
        
    def imprimir_curso(self):
        print(f"Curso del salon: {self.curso}")
        
    def imprimir_profesor(self):
        print(f"Profesor del salon: {self.profesor}")
        
    def imprimir_estudiantes(self):
        print("Estudiantes del salon:")
        for estudiante in self.estudiantes:
            print(estudiante)
    

