try: #Se crea el bloque de codigo para iniciar una excepcion y corregir el error.
    #print(1/1)) #Se imprime el error que queremos que aparesca en la ejecucion del codigo
    raise SyntaxError #El metodo raise corrige el error SyntaxError
except SyntaxError as e: #Se renombra la excepcion por una variable que en este caso la variable es e
    print(e) #Primero llama la excepcion para que ejecute su error el cual es SyntaxError
    print('Cierra el parentesis') #Imprime el mensaje que se vera al ejecutar cuando se llame la variable e
    
try: #Bloque de codigo que inicia una excepcion
    #raise ZeroDivisionError  #Va a imprimir la excepcion ZeroDivisionError pero sin ningun error del interprete
    print(1/0)#Si cualquier numero es 0 va arrojar la excepcion ZeroDivisionError
#except (ZeroDivisionError) as e: Se cambia la excepcion por una variable la cual esta asignada con la letra e
except ZeroDivisionError as zde: #Aqui tambien se le asigna otra variable pero esta vez llamada zde
    print(zde)#Llama la variable zde
    #print('prueba error') #pasa primero por la variable y luego imprime lo siguiente ("Prueba error")