
from Persona import Persona
from Estudiante import Estudiante
from Curso import Curso
from Materia import Materia


def main():
    # TODO: Add your code here

   #crear una instancia de la clase persona
    print("\n\n###### Persona ###############")
    persona = Persona("Juan", 30, "Colombia")
    
    #imprimir todos los datos de la persona
    persona.imprimir_datos()
    
    print("###### Fin Persona ###############\n")

    print("###### Estudiante ###############")

    #crear una instancia de la clase estudiante incluyendo la lista de estudiantes
    estudiante = Estudiante("Juan", 30, "Colombia")
    #imprimir todos los datos del estudiante
    estudiante.imprimir_datos()
    
    print("###### Fin Estudiante ###############\n")
    
 
    print("####### Profesor ###############")

    #crear una instancia de la clase profesor
    profesor = Persona("Pedro", 35, "Argentina")
   
    #imprimir todos los datos del profesor
    profesor.imprimir_datos()
    
    print("###### Fin Profesor ###############\n")


    print("###### Curso ###############")

    #crear una instancia de la clase curso
    curso = Curso("Python", "6 meses")

    #imprimir todos los datos del curso
    curso.imprimir_datos()

    print("###### Fin Curso ###############\n")


    print("###### Materia ###############")
    
    #crear una instancia de la clase materia, incluyendo el curso,profesor y estudiantes
    materia = Materia("Programacion", curso, profesor, [estudiante])
    #imprimir todos los datos de la materia
    materia.imprimir_nombre()
    materia.imprimir_curso()
    materia.imprimir_profesor()
    materia.imprimir_estudiantes()

    print("###### Fin Materia ###############\n")


    print("###### Grupo ###############")
    
    #crear una instancia de la clase grupo, incluyendo el curso,profesor y estudiantes
    grupo = Materia("Programacion", curso, profesor, [estudiante])
    #imprimir todos los datos del grupo
    grupo.imprimir_nombre()
    grupo.imprimir_curso()
    grupo.imprimir_profesor()
    grupo.imprimir_estudiantes()

    print("###### Fin Grupo ###############\n")

    print("###### Salon ###############")
    
    #crear una instacia de la clase salon, incluyendo grupo, curso, profesor y estudiantes
    salon = Materia("Programacion", curso, profesor, [estudiante])
    #imprimir todos los datos del salon
    salon.imprimir_nombre() 
    salon.imprimir_curso()
    salon.imprimir_profesor()
    salon.imprimir_estudiantes()

    print("###### Fin Salon ###############\n")

    print("###### Escuela ###############")

    #crear una instancia de la clase escuela, incluyendo salon, grupo, curso, profesor y estudiantes
    escuela = Materia("Programacion", curso, profesor, [estudiante])
    #imprimir todos los datos de la escuela
    escuela.imprimir_nombre()
    escuela.imprimir_curso()
    escuela.imprimir_profesor()
    escuela.imprimir_estudiantes()

    print("###### Fin Escuela ###############\n")

    print("###### Universidad ###############")
    
    #crear una instancia de la clase universidad, incluyendo escuela, salon, grupo, curso, profesor y estudiantes
    universidad = Materia("Programacion", curso, profesor, [estudiante])
    #imprimir todos los datos de la universidad
    universidad.imprimir_nombre()
    universidad.imprimir_curso()
    universidad.imprimir_profesor()
    universidad.imprimir_estudiantes()

    print("###### Fin Universidad ###############\n")

    

if __name__ == "__main__":
    main()