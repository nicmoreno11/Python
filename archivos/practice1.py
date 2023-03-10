from Aprendiz import * #se crea una importacion de la clase aprendiz
from Curso import * #se crea una importacion de la clase curso
with open('archivos/aprendices.txt','r') as flujo: #se crea un metodo para abrir el archivo desde la variable flujo y observar los cambios que se van a realizar y le decimos donde esta el archivo
    datos=flujo.read() #se crea una variable 'datos' se instancia la variable 'flujo' y se crea el metodo read para solo leer el archivo
    print(datos) #se imprime la variable 'datos'
    #flujo.write('2560664,maria,123') #se crea un metodo para poder escribir en el archivo el metodo es 'write'
aprendices=[] #se crea una lista para añadir todos los datos a ella
with open('archivos/aprendices.txt','r') as flujo: #se crea un metodo para abrir el archivo desde la variable flujo y observar los cambios que se van a realizar en este caso se va a crear todo como una lista la que se creo anteriomente
    for linea in flujo: #se crea un for parar recorrer los datos de la variable flujo y los muestra como una lista
        #print(linea) #imprime los datos recorridos de la lista
        aprendices.append(linea.rsplit()) #se agregan datos a la lista y se quita el '\n' que tiene cada elemento

datosxlinea=[] #se crea de nuevo una lista
for aprendiz in aprendices: #se crea una lista para agregar los datos que tiene aprendiz en aprendices
    datosxlinea.append(aprendiz[0].split(','))#añade los datos a la lista y recorre desde la posicion 0 cada uno de los datos y se quitan las comas que lleva cada dato y se toma cada dato como independiente

#print(ob.getNombre()) #imprime el objeto que quiere obtener

print(datosxlinea) #imprime todos los valores de la lista

listaDeObjetos=[] #se crea otra lista para cada uno de los objetos
for apr in datosxlinea: #recorre cada objeto que se agrega a la lista
     f=apr[0] #se crea la variable para asignar una posicion que va a recorrer el for
     n=apr[1] #aca igual se crea la variable para asignar la posiciob en la que va a recorrer el for
     d=apr[2] #se crea una varibale la cual tiene una posicion en la que va a recorrer el for
     ob=Aprendiz(f,n,d) #variable e instancia la clase y se le pasan parametros los cuales son (f,n,d)
     print(ob) #imprime la variable 'ob'
     listaDeObjetos.append(ob) #se agrega lo que tiene la variable a la lista vacia 'ListaDeObjetos'

for xx in listaDeObjetos: #se crea un for para recorrer la lista
    print(xx.getNombre()) #impresion para obtener el nombre del aprendiz
    print(xx.getDocumento()) #impresion para obtener el documento del aprendiz
    print(xx.getFicha())#impresion para obtener la ficha del aprendiz