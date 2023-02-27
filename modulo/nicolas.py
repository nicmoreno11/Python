def positivonegativo(numero):
    if numero == 0:
        return("cero")
    elif numero < 0:
        return("negativo")
    else:
        return("positivo")

def tiempo(t):
    m = t / 60
    h = m / 60
    return("horas: ", h), ("minutos: ", m), ("segundos: ", t)

t = int(input("ingrese el valor en segundos: "))
print(tiempo(t))

def resta(op1,op2):
	print("El resultado de la resta es: ", op1-op2)

def multiplicacion(op1,op2):
	print("El resultado de la multiplicacion es: ", op1*op2)

def es_multiplo(numero, multiplo):
    return numero % multiplo == 0


if es_multiplo(9, 3):
    print("Sí es múltiplo")
else:
    print("No es múltiplo")



