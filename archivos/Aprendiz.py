from Persona import *
#from Curso import * ...en caso de composición
class Aprendiz(Persona):
    def __init__(self,ficha,nombre,documento):
        Persona.__init__(self,nombre,documento)
        self.__ficha=ficha
        self.__cursos=[]
    def getFicha(self):
        return self.__ficha
    def setNombre(self,ficha):
        self.__ficha=ficha
    def agregarCurso(self,curso):
        #c=Curso('python',120)
        self.__cursos.append(curso)
    def getCursos(self):
        return self.__cursos