#crear un metodo que imprima el nombre de la universidad
#crear un metodo que imprima el salon de la universidad
#crear un metodo que imprima el grupo de la universidad
#crear un metodo que imprima el curso de la universidad
#crear un metodo que imprima el profesor de la universidad
#crear un metodo que imprima los estudiantes de la universidad
#crear una instancia de la clase universidad

class Universidad:
    def __init__(self, nombre, salon, grupo, curso, profesor, estudiantes):
        self.nombre = nombre
        self.salon = salon
        self.grupo = grupo
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes
        
    def imprimir_nombre(self):
        print(f"Nombre: {self.nombre}")
        
    def imprimir_salon(self):
        print(f"Salón:\n\t {self.salon.nombre}")
        
    def imprimir_grupo(self):
        print(f"Grupo:\n\t {self.grupo.nombre}")
        
    def imprimir_curso(self):
        print(f"Curso:\n\t Nombre: {self.curso.nombre}, Duración:{self.curso.duracion}")
        
    def imprimir_profesor(self):
        print(f"Profesor:\n\t Nombre: {self.profesor.nombre},Edad: {self.profesor.edad},País: {self.profesor.pais}")
        
    def imprimir_estudiantes(self):
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(f"\t Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, País: {estudiante.pais}")
    
