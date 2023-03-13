from pydoc import classname


class Actriz:
    def __init__(self,Index,Year,Age,Name,Movie):
        self.__Index=Index
        self.__Year=Year
        self.__Age=Age
        self.__Name=Name
        self.__Movie=Movie
    def nombreCompleto(self):
        return self.__Name+' '+self.__Movie