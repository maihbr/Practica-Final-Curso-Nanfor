class Persona:
    def __init__(self, nombre, edad, pais_origen):
        self.nombre = nombre
        self.edad = edad
        self.pais_origen = pais_origen

    def imprimir_nombre(self):
        print(f"Nombre: {self.nombre}")

    def imprimir_edad(self):
        print(f"Edad: {self.edad}")

    def imprimir_pais_origen(self):
        print(f"País de origen: {self.pais_origen}")

    def imprimir_datos(self):
        self.imprimir_nombre()
        self.imprimir_edad()
        self.imprimir_pais_origen()

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30, "España")

# Probar los métodos de la clase Persona
persona.imprimir_nombre()
persona.imprimir_edad()
persona.imprimir_pais_origen()
persona.imprimir_datos()

class Estudiante(Persona):
    def imprimir_nombre(self):
        print(f"Nombre del estudiante: {self.nombre}")

    def imprimir_edad(self):
        print(f"Edad del estudiante: {self.edad}")

    def imprimir_pais_origen(self):
        print(f"País de origen del estudiante: {self.pais_origen}")

    def imprimir_datos(self):
        self.imprimir_nombre()
        self.imprimir_edad()
        self.imprimir_pais_origen()

# Crear una instancia de la clase Estudiante
estudiante = Estudiante("Ana", 20, "México")
estudiante.imprimir_datos()


class Profesor(Persona):
    def imprimir_nombre(self):
        print(f"Nombre del profesor: {self.nombre}")

    def imprimir_edad(self):
        print(f"Edad del profesor: {self.edad}")

    def imprimir_pais_origen(self):
        print(f"País de origen del profesor: {self.pais_origen}")

    def imprimir_datos(self):
        self.imprimir_nombre()
        self.imprimir_edad()
        self.imprimir_pais_origen()

# Crear una instancia de la clase Profesor
profesor = Profesor("Carlos", 45, "Argentina")
profesor.imprimir_datos()

class Curso:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def imprimir_nombre(self):
        print(f"Nombre del curso: {self.nombre}")

    def imprimir_duracion(self):
        print(f"Duración del curso: {self.duracion}")

# Crear una instancia de la clase Curso
curso = Curso("Matemáticas", "3 meses")
curso.imprimir_nombre()
curso.imprimir_duracion()

class Materia:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_nombre(self):
        print(f"Nombre de la materia: {self.nombre}")

    def imprimir_curso(self):
        self.curso.imprimir_nombre()

    def imprimir_profesor(self):
        self.profesor.imprimir_nombre()

    def imprimir_estudiantes(self):
        print("Estudiantes de la materia:")
        for estudiante in self.estudiantes:
            estudiante.imprimir_nombre()

# Crear una instancia de la clase Materia
materia = Materia("Álgebra", curso, profesor, [estudiante])
materia.imprimir_nombre()
materia.imprimir_curso()
materia.imprimir_profesor()
materia.imprimir_estudiantes()

class Grupo:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_nombre(self):
        print(f"Nombre del grupo: {self.nombre}")

    def imprimir_curso(self):
        self.curso.imprimir_nombre()

    def imprimir_profesor(self):
        self.profesor.imprimir_nombre()

    def imprimir_estudiantes(self):
        print("Estudiantes del grupo:")
        for estudiante in self.estudiantes:
            estudiante.imprimir_nombre()

# Crear una instancia de la clase Grupo
grupo = Grupo("Grupo A", curso, profesor, [estudiante])
grupo.imprimir_nombre()
grupo.imprimir_curso()
grupo.imprimir_profesor()
grupo.imprimir_estudiantes()

class Salon:
    def __init__(self, nombre, grupo):
        self.nombre = nombre
        self.grupo = grupo

    def imprimir_nombre(self):
        print(f"Nombre del salón: {self.nombre}")

    def imprimir_grupo(self):
        self.grupo.imprimir_nombre()

    def imprimir_curso(self):
        self.grupo.imprimir_curso()

    def imprimir_profesor(self):
        self.grupo.imprimir_profesor()

    def imprimir_estudiantes(self):
        self.grupo.imprimir_estudiantes()

# Crear una instancia de la clase Salon
salon = Salon("Salón 101", grupo)
salon.imprimir_nombre()
salon.imprimir_grupo()
salon.imprimir_curso()
salon.imprimir_profesor()
salon.imprimir_estudiantes()

class Escuela:
    def __init__(self, nombre, salon):
        self.nombre = nombre
        self.salon = salon

    def imprimir_nombre(self):
        print(f"Nombre de la escuela: {self.nombre}")

    def imprimir_salon(self):
        self.salon.imprimir_nombre()

    def imprimir_grupo(self):
        self.salon.imprimir_grupo()

    def imprimir_curso(self):
        self.salon.imprimir_curso()

    def imprimir_profesor(self):
        self.salon.imprimir_profesor()

    def imprimir_estudiantes(self):
        self.salon.imprimir_estudiantes()

# Crear una instancia de la clase Escuela
escuela = Escuela("Escuela Primaria", salon)
escuela.imprimir_nombre()
escuela.imprimir_salon()
escuela.imprimir_grupo()
escuela.imprimir_curso()
escuela.imprimir_profesor()
escuela.imprimir_estudiantes()

class Universidad:
    def __init__(self, nombre, salon):
        self.nombre = nombre
        self.salon = salon

    def imprimir_nombre(self):
        print(f"Nombre de la universidad: {self.nombre}")

    def imprimir_salon(self):
        self.salon.imprimir_nombre()

    def imprimir_grupo(self):
        self.salon.imprimir_grupo()

    def imprimir_curso(self):
        self.salon.imprimir_curso()

    def imprimir_profesor(self):
        self.salon.imprimir_profesor()

    def imprimir_estudiantes(self):
        self.salon.imprimir_estudiantes()

# Crear una instancia de la clase Universidad
universidad = Universidad("Universidad Nacional", salon)
universidad.imprimir_nombre()
universidad.imprimir_salon()
universidad.imprimir_grupo()
universidad.imprimir_curso()
universidad.imprimir_profesor()
universidad.imprimir_estudiantes()