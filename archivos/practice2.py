from archivos.Aprendiz import Aprendiz
from Aprendiz import* #se importan los datos de aprendiz
from Curso import* #se importan los datos de curso
nombre=input('ingrese nombre del aprendiz')#se crea una variable nombre para poder ingresar el nombre del aprendiz
documento=int(input('ingrese documento del aprendiz')) #se crea una variable documento para poder ingresar el documento del aprendiz
ficha=input('ingrese ficha del aprendiz') #se crea una variable ficha para poder ingresar el numero de ficha del aprendiz

ap=Aprendiz(ficha,nombre,documento) #se crea una variable que instancia la clase Aprendiz con los parametros (ficha,nombre,documento)

nombreCurso=input('ingrese nombre del curso') #se crea una variable para ingresar el nombre del curso
horas=int(input('ingrese intensidad horaria del curso'))#se crea otra variable 'hora' para que ingrese la cantidad de horas que dura el curso
c1=Curso(nombreCurso,horas) #se crea una instancia con los parametros (nombrecurso y horas)
ap.agregarCurso(c1)#se utiliza el metodo agregar curso del objeto ap y le pasa como argumento 'c1'

with open('archivos/aprendices.txt','a') as flujo: #metodo para que se hagan modificacion en el archivo de texto (aprendices.txt)
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n') #se pasan todos los datos de la clase aprendiz