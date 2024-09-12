#crear un metodo que imprima el nombre de la escuela
#crear un metodo que imprima el salon de la escuela
#crear un metodo que imprima el grupo de la escuela
#crear un metodo que imprima el curso de la escuela
#crear un metodo que imprima el profesor de la escuela
#crear un metodo que imprima los estudiantes de la escuela
#crear una instancia de la clase escuela

class Escuela:
    def __init__(self, nombre, salon, grupo, curso, profesor, estudiantes):
        self.nombre = nombre
        self.salon = salon
        self.grupo = grupo
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes
        
    def imprimir_nombre(self):
        print(f"Nombre de la escuela: {self.nombre}")
        
    def imprimir_salon(self):
        print(f"Salon de la escuela: {self.salon}")
        
    def imprimir_grupo(self):
        print(f"Grupo de la escuela: {self.grupo}")
        
    def imprimir_curso(self):
        print(f"Curso de la escuela: {self.curso}")
        
    def imprimir_profesor(self):
        print(f"Profesor de la escuela: {self.profesor}")
        
    def imprimir_estudiantes(self):
        print("Estudiantes de la escuela:")
        for estudiante in self.estudiantes:
            print(estudiante)
    
