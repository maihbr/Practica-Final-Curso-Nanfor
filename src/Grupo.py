class Grupo:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes
        
    def imprimir_nombre(self):
        print(f"Nombre del grupo: {self.nombre}")
        
    def imprimir_curso(self):
        print(f"Curso del grupo: {self.curso}")
        
    def imprimir_profesor(self):
        print(f"Profesor del grupo: {self.profesor}")
        
    def imprimir_estudiantes(self):
        print("Estudiantes del grupo:")
        for estudiante in self.estudiantes:
            print(estudiante)

