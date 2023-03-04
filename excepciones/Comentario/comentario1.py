class Vehiculo: #Se crea una clase padre Vehiculo
    def __init__(self,tipo): #Se inicia el constructor de la clase padre
        self.tipo=tipo
    def descripcion(self): #Se crea una funcion para dar como descripcion que tipo de vehiculo es
        print('Soy generico no tengo descripcion',self.tipo)#Imprime la descripcion del tipo de vehiculo
#v=Vehiculo('Cualquier tipo') #Se asigna una descripcion por si mismo (independiente)

    def getTipo(self): #obtener el valor de que tipo de vehiculo es
        return self.tipo #retorna y devuelve el valor el cual es tipo
        #return Vehiculo.tipo
    def __str__(self): #es el metodo que va a buscar en cada una de las clases si ese valor retornado es verdad o es falso 
        return 'Soy objeto de la clase Vehiculo' #retorna y imprime 'Soy objeto de la clase Vehiculo' si esto es 
    
    

class Herramienta: #Se crea una clase hija Herramienta
    def __init__(self,proposito): #Se inicia el constructor de la clase hija 
        self.__proposito=proposito #obtiene un valor de la clase hija y propio de la clase padre
    def getProposito(self): #obtener el proposito y descripcion del vehiculo
        return self.__proposito #retorna el valor en este caso (proposito)
    def __str__(self): #tambien se da el valor str para verificar que ese valor retornado esta en una de las clases ya sea hija o padre 
        return 'Soy objeto de la clase Herramienta'
class Terrestre(Vehiculo,Herramienta): #se crea otra subclase en este caso con las subclases terrestre y herramienta anidados a la clase padre la cual es vehiculo
    def __init__(self,tipo,proposito): #se inicia el constructor con el metodo self se le asigna los valores tipo y proposito ya asignados anteriormente
        Herramienta.__init__(self,proposito) #se crea un constructor con el metodo str con el valor propio proposito asignado a esa clase propia
        Vehiculo.__init__(self,tipo) #sucede lo mismo en caso de ser herramienta es vehiculo con su valor propio que es tipo y imprime que tipo         
    def datos(self):
        print('Tipo: ',super().getTipo())
        print('Tipo: ',super().getProposito())
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())