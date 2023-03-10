class Curso:
    def __init__(self,nombre,horas):
        self.__nombre=nombre
        self.__horas=horas
    def getNombre(self):
        return self.__nombre