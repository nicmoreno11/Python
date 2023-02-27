def recurcivo():
    try:
        entero = int(input("Ingrese un numero entero: "))
        assert entero % 2 == 0
        print("Divisor de 2")

    except AssertionError:
        print("Debe ingresar un numero par")
        recurcivo()
recurcivo()