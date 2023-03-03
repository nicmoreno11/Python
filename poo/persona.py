
class Persona: #Se crea una clase con el nombre personas
    def __init__(self,nombre,documento): #Constructor que tiene dos datos 
        self.__nombre=nombre
        self.__documento=documento #Tiene una herencia que hace parte de la clase padre
        #print('Constructor Activado')

    def getNombre(self): #Se crea una funcion para visualizar el nombre.
        return self.__nombre #retorna y devuelve el nombre que le asignan

    def setNombre(self,nombre):
        self.__nombre=nombre
    def getDocumento(self):
        return self.__documento
ob=Persona('Maria') #Se llama la clase y se le define un atributo a la clase persona (nombre)
print(ob.getNombre()) #Imprime el objeto dentro de la clase en este caso es ("Maria")
ob.setNombre('Ana') #Imprime el objeto ya asigando
print(ob.getNombre()) #Llama los dos objetos e imprime (Ana y Maria)
#print(type(ob))

#Ejercicio asignado por el instructor.
class Aprendiz(Persona): #Se crea la subclase Aprendiz
    def __init__(self,nombre,ficha,documento):
        Persona.__init__(self,nombre)
        self.__ficha=ficha
        Persona.__init__(self,documento)
        self.__documento=documento
    def getFicha(self):
        return self.__ficha
    
    def getdocumento(self):
        return self.__documento
    
    def getNombre(self):
        return self.__nombre
    
    
def all(self):
        print(self.getNombre())
        print(self.getFicha())
        print(self.getdocumento)

app=Aprendiz('Pedro',12345,1025522433)
print(app.getFicha())
print(app.getNombre)
print(app.getdocumento())

#def datosinstancia(self):
    #print("nombre tipo de dato"type(self.__nombre))
    #print("documento tipo de dato"type(self.__documento))
#Atributo es lo mismo que variable de instancia o tambien como una propiedad
