#Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
def cadena():
    cadena = "aaabcdefghijklmnñopqrstuvxyz"
    caracteres = len(cadena)
    print(caracteres)
#cadena()

def repetidas():
        print("aaabcdefghijklmnñopqrstuvxyz".count("a"))
#repetidas()

#pida una cadena por teclado y diga cual es su valor al sumar sus codigos
"""def cadena():
    cadena = input("Ingrse el nombre que le quiere dar a la cadena: ")
for caracter in cadena:
    suma_codigos = 0
    suma_codigos += ord(caracter)
    print("La suma de los codigos de caracteres de la cadena es:", suma_codigos)"""
#cadena()

#Cual es el valor numerico de acuerdo a los códigos del alfabeto
def valor_letra(letra):
    if letra.isupper():
        valor = ord(letra) - ord('A') + 1
    elif letra.islower():
        valor = ord(letra) - ord('a') + 1
    else:
        valor = None
    return valor

def valornumerico():
    valor = "a"
    valor2 = "b"
    print(ord(valor))
    print(ord(valor2))
#valornumerico()

#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas

def cadena():
    cadena = input("Ingrese una palabra o frase: ")
    print("La cadena en mayusculas es", cadena.upper())
    print("La cadena en minusculas es", cadena.lower())
    print("Cadena en forma de titulo", cadena.title())
#cadena()

# Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
def ortografia(c):
    if(c[-1]==225 or c[-1]==233 or c[-1]==237 or c[-1]==243 or c[-1]==233 or c[-1]==250):
        print("aguda")
    else:
        print("No es aguda")
#ortografia("café")

def es_grave(palabra):
    palabra = "fútbol"
    palabra = palabra.lower()
    ultima_vocal = -1
    for i in range(len(palabra)):
        if palabra[i] in "aeiouáéíóú":
            ultima_vocal = i
        if ultima_vocal == -1:
            return False

        if ultima_vocal == len(palabra) -1:
            return True
        elif ultima_vocal == len(palabra) -2  and palabra[-1] not in "ns":
            return False
#es_grave()

#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def cadena():
    cadena = "¡Hola, cómo estás? ¿Todo bien?"

vocales = 0
consonantes = 0
vocales_tilde = 0
especiales = 0

for caracter in cadena:
    caracter = caracter.lower()
    
    if caracter in "aeiou":
        vocales += 1
        
        if caracter in "áéíóú":
            vocales_tilde += 1
    elif caracter.isalpha():
        consonantes += 1
    else:
        especiales += 1

print(f"La cadena tiene {vocales} vocales, {consonantes} consonantes, {vocales_tilde} vocales con tilde y {especiales} caracteres especiales.")

# cuantas veces se repite un caracter dado
def cadena(letra):
    cadena = "mamá"  
caracter = "a"
contador = 0
for letra in cadena:
        if letra == caracter:
            contador += 1
#print(f"El carácter '{caracter}' aparece {contador} veces en la cadena '{cadena}'.")