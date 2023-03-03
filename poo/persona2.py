class Persona:
    def __init__(self,nombre):
        self.__nombre=nombre
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))
#Self metodo 
#Ejercicio asignado por el profesor.

class Aprendiz(Persona):
    def __init__(self,nombre,ficha,documento):
        Persona.__init__(self,nombre)
        self.__ficha=ficha
        Persona.__init__(self,documento)
        self.__documento=documento
    def getFicha(self):
        return self.__ficha
    
    def getdocumento(self):
        return self.__documento
    
def all(self):
        print(self.getNombre())
        print(self.getFicha())
        print(self.getdocumento)

app=Aprendiz('Pedro',12345,1025522433)
print(app.getFicha())
print(app.getNombre)
print(app.getdocumento())
print(app.all())
