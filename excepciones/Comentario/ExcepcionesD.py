def edad(): #Se crea una funcion llamada edad 
    try: #Se crea una excepción 
        tuedad=int(input("introduce tu edad")) #Se crea una variable llamada tu edad y solo permite valores enteros(solo numeros no caracteres como un texto o una letra de lo contrario ejecutara errror)
        print(f'tu edad es  {tuedad}') #Se imprime la variable tuedad
        #print('Tu edad es ',tuedad) #Sucede lo mismo y la forma de ejecucion es la misma dara el mismo resultado
    except ValueError as e: #La excepcion ValueError va a verificar el valor de la variable es numerico o es un valor de caracteres (str)
        print(e)#Imprime la excepcion ValueError asignada con la letra(e)
        print("La edad debe ser un valor numerico...")#Advierte que el valor de la edad tiene que ser un valor numerico no puede ser una cadena de caracteres
        edad()#Llama la funcion dentro de la excepcion y lo toma argumento con ningun valor mientras estee dentro de la excepcion, es funcion recurciva

edad()#Se llama la funcion