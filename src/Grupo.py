class Grupo:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes
        
    def imprimir_nombre(self):
        print(f"Grupo: {self.nombre}")
        
    def imprimir_curso(self):
        print(f"Curso del grupo:\n\t Nombre : {self.curso.nombre}, Duración : {self.curso.duracion}")
        
    def imprimir_profesor(self):
        print(f"Profesor del grupo:\n\t Nombre: {self.profesor.nombre}, Edad: {self.profesor.edad}, País {self.profesor.pais}")
        
    def imprimir_estudiantes(self):
        print("Estudiantes del grupo:")
        for estudiante in self.estudiantes:
            print(f"\t Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, País {estudiante.pais}")

