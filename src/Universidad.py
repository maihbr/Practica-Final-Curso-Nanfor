#crear un metodo que imprima el nombre de la universidad
#crear un metodo que imprima el salon de la universidad
#crear un metodo que imprima el grupo de la universidad
#crear un metodo que imprima el curso de la universidad
#crear un metodo que imprima el profesor de la universidad
#crear un metodo que imprima los estudiantes de la universidad
#crear una instancia de la clase universidad

class Universidad
    def __init__(self, nombre, salon, grupo, curso, profesor, estudiantes):
        self.nombre = nombre
        self.salon = salon
        self.grupo = grupo
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes
    
    def imprimir_nombre(self):
        print(f"Nombre de la universidad: {self.nombre}")
    
    def imprimir_salon(self):
        print(f"Salon de la universidad: {self.salon}")
    
    def imprimir_grupo(self):
        print(f"Grupo de la universidad: {self.grupo}")
    
    def imprimir_curso(self):
        print(f"Curso de la universidad: {self.curso}")
    
    def imprimir_profesor(self):
        print(f"Profesor de la universidad: {self.profesor}")

    def imprimir_estudiantes(self):
        print("Estudiantes de la universidad:")
        for estudiante in self.estudiantes:
            print(estudiante)



