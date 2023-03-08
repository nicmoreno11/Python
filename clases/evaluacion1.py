class Libro:
    def __init__(self,titulo,tipo,autor,editorial):
        self.titulo=titulo
        self.tipo=tipo
        self.autor=autor
        self.editorial=editorial
    def getTitulo(self):
        return self.titulo
    def getTipo(self):
        return self.tipo
    def setAutor(self,autor):
        self.autor=autor
    def getAutor(self):
            return self.autor
    def setEditorial(self,editorial):
        self.editorial=editorial
    def getEditorial(self):
            return self.editorial
n= Libro('carrie','novela','Stephen King', 'doubleday')
#print(n.getAutor())
#n.setEditorial('Penguin Libros')
#n.setAutor('garcia marquez')

class Revista:
    def __init__(self,titulo,tipo,autor,edicion):
        self.titulo=titulo
        self.tipo=tipo
        self.autor=autor
        self.edicion=edicion
    def getTitulo(self):
        return self.titulo
    def getTipo(self):
        return self.tipo
    def setAutor(self,autor):
        self.autor=autor
    def getAutor(self):
        return self.autor
    def setEdicion(self,edicion):
        self.edicion=edicion
    def getEdicion(self):
        return self.edicion

r=Revista('Rolling Stone', 'cultura','Rolling Stones', 'Col-Rolling Stone en español')
#print(r.getTipo())
#print(r.getAutor())
#r.setEdicion('Por-Rolling Stone en portugues')
class Lector:
    def __init__(self,nombre,direccion,telefono,email):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__email=email
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getEmail(self):
        return self.__email
l=Lector("pepe","cl21sur",'3049211',"pepe@gmail.com")
#print(l.getEmail())

class Docente(Lector):
    def __init__(self,codigo,nombre,direccion,telefono,email):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__email=email
    def getCodigo(self):
        return self.__codigo
    def setCodigo(self,codigo):
        self.__codigo=codigo
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getEmail(self):
        return self.__email
a=Docente(234123,"luis","calle21","3456321","luis@gmail.com")
#print(a.getNombre())
#print(a.getCodigo())
#a.setNombre('luisa')
class Estudiante(Lector):
    def __init__(self,codigo):
        self.__codigo=codigo
    def getCodigoE(self):
        return self.__codigo
    def setCodigoE(self,codigo):
        self.__codigo=codigo
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getEmail(self):
        return self.__email
e=Lector('andres', 'calle23norte','3201902','andres@gmail.com')
#print(e.getNombre())
#e.setNombre('nicolas')

class Blibliotecario(Lector):
    def __init__(self,idPersonal):
        self.__idPersona=idPersonal
    def getIdPersona(self):
        return self.__idPersona
    def setidPersona(self,idPersona):
        self.__idPersona=idPersona
p=Blibliotecario(3429391193)
#print(p.getIdPersona())
#p.setidPersona('299032829')
class Pedido(Libro,Revista):
    def __inint__(self,titulo,tipo,autor,edicion,editorial):
        self.__id=id
        self.titulo=titulo
        self.tipo=tipo
        self.autor=autor
        self.edicion=edicion
        self.editorial=editorial
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
    def getTitulo(self):
        return self.titulo
    def setTitulo(self,titulo):
        self.titulo=titulo
    def getAutor(self):
        return self.autor
    def setAutor(self,autor):
        self,autor=autor
    def getEdicion(self):
        return self.edicion
    def getEditorial(self):
        return self.edicion
    def getEditorial(self):
        return self.editorial
n= Libro('carrie','novela','Stephen King', 'doubleday')
r=Revista('Rolling Stone', 'cultura','Rolling Stones', 'Col-Rolling Stone en español')
#print(getall())       
#print(n.getTitulo())
#print(n.getAutor())
#n.setAutor('stephen hawking')

class Pedido(Lector):
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
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
p=Pedido(12345,'carrie',34211)
#print(p.getTitulo())
#print(p.getCodigo())
#print(p.getId())

def Menu(n): 
    n= Libro('carrie','novela','Stephen King', 'doubleday')
    while True:
        print('1-obtener informacion del libro: ',Libro)
        print('2-obtener informacion del docente: ',Docente)
        print('3-obtener informacion del estudiante: ',Estudiante)
        print('4-obtener informacion de la revista: ',Revista)
        print('5-obtener informacion del lector: ',Lector)
        print('6-obtener informacion del bibliotecario',Blibliotecario)
        print('7-Salir')

        ctrl=int(input('Ingrese la opcion: '))
        match ctrl:
            case 1:
                print('ingreso 1',n.getEditorial(),'esta es la edicion',n.getAutor(),'este es el autor',n.getTipo(),'este es el tipo del libro')
            case 2:
                print('ingreso 2')
            case 3:
                print('ingreso 3')
            case 4:
                print('ingreso 4')
            case 5:
                print('ingreso 5')
            case 6:
                print('ingreso 6')
            case 7:
                print('salir')
            case _:
                print('no existe')
#print(Menu(Libro))
#print(Menu(Docente))
#f=0
#print(Clase(f))