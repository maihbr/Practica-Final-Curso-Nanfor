class Materia:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes
        
    def imprimir_nombre(self):
        print(f"Nombre de la materia: {self.nombre}")
        
    def imprimir_curso(self):
        print(f"Curso de la materia: {self.curso}")
        
    def imprimir_profesor(self):
        print(f"Profesor de la materia: {self.profesor}")
        
    def imprimir_estudiantes(self):
        print("Estudiantes de la materia:")
        for estudiante in self.estudiantes:
            print(estudiante)

