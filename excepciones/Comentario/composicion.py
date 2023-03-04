class Curso: #Se crea la clase curso
    def __init__(self,titulo): #se crea el constructor de la clase padre
        self.__titulo=titulo

    def getTitulo(self): #se crea una funcion para obtener el titulo (nombre) del curso 
           return self.__titulo #retorna y imprime el titulo cuando ya se llame la funcion 

class Aprendiz: #Se crea una subclase esta vez llamada aprendiz
    def __init__(self,nombre): #Se crea el constructor de la subclase
        self.__nombre=nombre
        self.__cursos=[] #se hace una lista vacia para agregar valores a ella 

    def agregarCurso(self,nombreCursito): #se crea una funcion para poder asi agregar un curso a la clase principal en este caso es curso
        cursito=Curso(nombreCursito) #variable para asignarle el nombre al curso 
        self.__cursos.append(cursito) #la asignacion es propia pero depende de la clase curso 

    def getCursos(self): #crea una funcion para visualizar los cursos asignados a la clase padre
        return self.__cursos #retorna y imprime el nombre de los cursos
    
ap=Aprendiz('Sofia') #Llamando la funcion con una variable asignada y se le agrega el nombre del aprendiz
ap.agregarCurso('Python Basico') #llamando la funcion dentro de la clase curso pero con la misma varible ya que depende de la clase curso y se le asigna el nombre del curso
ap.agregarCurso('Python Intermedio') #es igual pero cambia el nombre del curso 

for c in ap.getCursos():  #se crea un for para recorrer cada uno de los cursos
    print(c.getTitulo()) #imprime y visulizaremos el nombre de cada uno de los cursos

del ap #se elimina la clase aprendiz.