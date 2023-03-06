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
l=Lector("pepe","cl21sur",3049211,"pepe@gmail.com")
#print(l.getEmail())

class Docente(Lector):
    def __init__(self,codigo):
        self.__codigo=codigo
    def getCodigo(self):
        return self.__codigo
    def setCodigo(self,codigo):
        self.__codigo=codigo
    def datos(self):
            return self.__nombre+int(self.__codigo)
#print(c.getCodigo())


class Estudiante(Lector):
    def __init__(self,codigo):
        self.__codigo=codigo
    def getCodigoE(self):
        return self.__codigo
    def setCodigoE(self,codigo):
        self.__codigo=codigo
e=Lector('andres', 'calle23norte',3201902,'andres@gmail.com')
#print(e.getNombre())

class Blibliotecario(Lector):
    def __init__(self,idPersona):
        self.__idPersona
    def getIdPersona(self):
        return self.__idPersona
    def setidPersona(self,idPersona):
        self.__idPersona=idPersona
class Pedido(Libro,Revista):
    def __inint__(self,id,titulo,codigo):
        self.__id=id
        self.titulo=titulo
        self.__codigo=codigo
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
    def getTitulo(self):
        return self.titulo
    def setTitulo(self,titulo):
        self.titulo=titulo
#print(n.getTitulo())

