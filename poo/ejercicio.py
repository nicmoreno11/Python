class producto():
    def __init__(self,nombre):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
ob=producto("nevera")
print(ob.getNombre())

class precio(producto):
    def __init__(self,nombre,precio):
        precio.__init__(self,nombre)
        self.__nombre=nombre
        precio.__init__(self,precio)
        self.__precio=precio
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    
producto1=producto("nevera",12000000)
print(producto1.getNombre())
producto2=precio("computador",1500000)
print(producto2.getPrecio())
producto3=precio("mouse",500000)
print(producto3.getNombre())






#calcular iva 
#def iva(self)
#i=self.__precio*0.19
#iva=self.__precio+1
#return"f{self.__precio} tiene un iva de {iva}"