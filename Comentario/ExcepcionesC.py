def try_syntax(numerator, denominator): #Se crea un funcion llamada try_syntax para detterminar si es un valor numerico o un caracter como valor
    try:
        print(f'In the try block: {numerator}/{denominator}')# Imprime los parametros numerator y denominator utilizando como syntaxis str en ("In try block")
        #quiero ver el resultado de la operacion en el print #print("In try bloc", numerator, denominator)
        result = numerator / denominator #Se crea una variable con sus dos argumentos numerator y denominator
    except ZeroDivisionError as zde: #Se crea una excepcion ZeroDivisionError en caso de que el valor sea cero y se renombra con la varibale zde
        print(zde) #Imprime la variable zde
    else: #Si el resultado no es cero va a imprimir el resultado de result = numerator / denominator
        print('The result is:', result) #Imprime el resultado de result = numerator / denominator
        return result #Va a retornar la variable result
    finally: #Retorna el resultado y sale de la ejecucion, pero si el valor es cero no retorna nada y imprime division by zero 
        print('Exiting')#Imprime saliendo en este caso hace el retorno
        #return "Fallo por zero"
print(try_syntax(12, 4)) #Imprime la funcion (try_syntax) con los parametros ya asignados
#print(try_syntax(11, 'a')) #Va a salir un error de ejecucion ya que esta haciendo una opracion de caracteres con valores numericos en este caso (10,'a')