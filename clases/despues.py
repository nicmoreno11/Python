"""class Pedido(Lector):
    def __init__(self, id, titulo, codigo):
        self.__id=id
        self.titulo=titulo
        self.__codigo=codigo
    def getId(self):
        return self.__id
    def serId(self,id):
        self.__id=id
    
    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo=titulo
    def getCodigo(self):
        return self.__codigo
    def setCodigo(self,codigo):
        self.__codigo=codigo

p=Pedido('12345','carrie','34211')
#print(p.getTitulo())"""

#Menu
"""def Clase(): 
    while True:
        print('1-obtener informacion del libro: ',Libro)
        print('2-obtener informacion del docente: ',Docente)
        print('3-obtener informacion del estudiante: ',Estudiante)
        print('4-obtener informacion de la revista: ',Revista)
        print('5-obtener informacion del libro: ',Libro)
        print('6-Salir')

        ctrl=int(input('Ingrese la opcion: '))
        match ctrl:
            case 1:
                print('ingreso 1')
            case 2:
                print('ingreso 2')
            case 3:
                print('ingreso 3')
            case 4:
                print('ingreso 4')
            case 5:
             print('ingreso 5')
            case _:
                print('no existe')
print(Clase(Docente))"""
"""def getall(self):
        self.titulo
        self.tipo
        self.edicion
        self.editorial
        self.autor"""




'''class Persona:
    nacionalidad='Colombia'    
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
    # def __init__(self):
    #     self.nombre=''
    #     self.documento=0
    def datosinstancias(self):
        print('nombre: tipo de dato',type(self.__nombre))
        print('documento: tipo de dato',type(self.__documento))

    def datos(self):
        return self.__nombre+str(self.documento)
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    

ob1=Persona('ana',123)
ob2=Persona('Luis',321)
ob2.correo='luis@mail.com'
ob2.datosinstancias()
print(ob2.getNombre())
ob2.setNombre('Pedro')
print(ob2.getNombre())
print(ob2.correo)'''



