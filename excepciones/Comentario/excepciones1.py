def lista():

    Lista=["Metallica","Crypta","Judas Priest","Burning witches","Guns N' Roses","Black veil brides"]
    buscar=int(input("Ingrese el índice con el que desea buscar: "))
    índice=8
    try:
        print(Lista[buscar])

    except IndexError:
        print("No se encuentra")
    else:
        print("Ingrese de nuevo el valor que quiere buscar",buscar)
lista()

