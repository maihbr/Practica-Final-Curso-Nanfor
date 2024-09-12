
from Persona import Persona
from Estudiante import Estudiante
from Curso import Curso
from Materia import Materia
from Grupo import Grupo
from Salon import Salon
from Escuela import Escuela
from Universidad import Universidad


def main():
    # TODO: Add your code here

   #crear una instancia de la clase persona
    print("\n\n############### Persona ###############")
    persona = Persona("Juan", 30, "Colombia")
    
    #imprimir todos los datos de la persona
    persona.imprimir_datos()
      
    print("\n\n############### Estudiante ###############")

    #crear una instancia de la clase estudiante incluyendo la lista de estudiantes
    estudiante = Estudiante("Juan", 30, "Colombia")
    #imprimir todos los datos del estudiante
    estudiante.imprimir_datos()
   
    print("\n\n####### Profesor ###############")

    #crear una instancia de la clase profesor
    profesor = Persona("Pedro", 35, "Argentina")
   
    #imprimir todos los datos del profesor
    profesor.imprimir_datos()
   
    print("\n\n########## Curso ###############")

    #crear una instancia de la clase curso
    curso = Curso("Python", "6 meses")

    #imprimir todos los datos del curso
    curso.imprimir_datos()

    print("\n\n###### Materia ###############")
    
    #crear una instancia de la clase materia, incluyendo el curso,profesor y estudiantes
    materia = Materia("Programación", curso, profesor, [estudiante])
    #imprimir todos los datos de la materia
    materia.imprimir_nombre()
    materia.imprimir_curso()
    materia.imprimir_profesor()
    materia.imprimir_estudiantes()

    
    print("\n\n ###### Grupo ###############")
    
    #crear una instancia de la clase grupo, incluyendo el curso,profesor y estudiantes
    grupo = Grupo("Grupo-Programación", curso, profesor, [estudiante])
    #imprimir todos los datos del grupo
    grupo.imprimir_nombre()
    grupo.imprimir_curso()
    grupo.imprimir_profesor()
    grupo.imprimir_estudiantes()

    
    print("\n\n###### Salón ###############")
    
    #crear una instacia de la clase salon, incluyendo grupo, curso, profesor y estudiantes
    salon = Salon("Salón-Programación",grupo, curso, profesor, [estudiante])
    #imprimir todos los datos del salon
    salon.imprimir_nombre() 
    salon.imprimir_grupo()
    salon.imprimir_curso()
    salon.imprimir_profesor()
    salon.imprimir_estudiantes()

    
    #crear una instancia de la clase escuela, incluyendo salon, grupo, curso, profesor y estudiantes
    escuela = Escuela("Escuela-Programación",salon,grupo,curso, profesor, [estudiante])
    print("\n\n###### Escuela ###############")
    #imprimir todos los datos de la escuela    
    escuela.imprimir_nombre()
    escuela.imprimir_salon()
    escuela.imprimir_grupo()
    escuela.imprimir_curso()
    escuela.imprimir_profesor()
    escuela.imprimir_estudiantes()

    print("\n\n###### Universidad ###############")    
    #crear una instancia de la clase universidad, incluyendo escuela, salon, grupo, curso, profesor y estudiantes
    universidad = Universidad("Universidad-Programación",salon,grupo, curso, profesor, [estudiante])        
    universidad.imprimir_nombre()
    universidad.imprimir_salon()
    universidad.imprimir_curso()
    universidad.imprimir_profesor()
    universidad.imprimir_estudiantes()



    

if __name__ == "__main__":
    main()