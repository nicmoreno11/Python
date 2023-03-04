class Aprendiz: #se crea una clase
    def __init__(self,nombre): #se crea el constructor de la clase
        self.__nombre=nombre
        self.__cursos=[] #se crea una lista vacia
    def agregarCurso(self,nombreCurso): #se crea una fucion para asignar valores a la lista
        self.__cursos.append(nombreCurso) #se pueden asignar mas valores a lista vacia
    def verCursos(self): #se crea una funcion para poder visualizar los cursos que se asignarion a la clase
        return self.__cursos #retorna y nos imprime cursos para poderlos visualizar 

class Curso: #se crea una subclase esta vez con el nombre curso 
    def __init__(self,nombreCurso): #se crea el constructor de la subclase
        self.__nombreCurso=nombreCurso

    def getNombreCurso(self):#se crea una funcion para poder obtener infomacion del nombre del curso
        return self.__nombreCurso #retona los valores
    
ob=Aprendiz('Miguel') #se crea una variable con el nombre del aprendiz ya asignado
c1=Curso('Python Basico') #se crean tres variables con los cursos asignados, pero con nombres diferentes
c2=Curso('Python Intermedio')
c3=Curso('Java Basico')

ob.agregarCurso(c1) #se llama la funcion con sus variables asignadas
ob.agregarCurso(c2)
ob.agregarCurso(c3)

for curso in ob.verCursos(): #se crea un for para recorrer los cursos y poder visualizarlos 
    print(curso.getNombreCurso()) #imprime el nombre de los cursos y obtiene el valor de ellos 

del ob #aca se elimina la clase curso
#print(ob) #se imprime la clase eliminada pero ejecuta un error ya que la clase no existe
print('.....',c1.getNombreCurso()) #se imprime el valor que existe en la varibale c1

