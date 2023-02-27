#Excepcion KeyError
diccionario = {"Vaca": "cow", "Caballo": "Horse", "Perro": "Dog", "Delfin": "Dolphin"}
def clave():
    try:
        buscar=input("Ingrese la clave que desea buscar: ")
        print(diccionario[buscar])
    except KeyError:
        print("La clave no existe")
    else:
        print("El valor de la clave es",diccionario)
clave()