from webbrowser import get


class Actor:
    def __init__(self,Index,Year,Age,Name,Movie):
        self.__Index=Index
        self.__Year=Year
        self.__Age=Age
        self.__Name=Name
        self.__Movie=Movie
    def getIndex(self):
        return self.__Index
    def getYear(self):
        return self.__Year
    def getAge(self):
        return self.__Age
    def getName(self):
        return self.__Name
    def getMovie(self):
        return self.__Movie
    def nombreCompleto(self):
        return self.__Name+' '+self.__Movie