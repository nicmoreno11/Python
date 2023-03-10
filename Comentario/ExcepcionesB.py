values = (1, 0) #Se crea una tupla con dos valores ya asignados
#x,y=10,12 #Aqui se crean dos valore y se le agragan dos variables diferentes a la de la tupla pero el resultado sera diferente
print(divmod(10,3)) #Se imprime el cociente y divisior en este caso seria 3 y 1
try: #Se empieza una excepcion para determinar si el valor es incorrecto o nulo
    q, r = divmod(*values) #Se separa por valor y se le asigna (q) y (r)
    #print('valor de q=',q) #Es el mismo caso pero en este caso se le esta asignando un valor independientemente a la variable q
    print(f'q={q}')#imprime las variables con el valor asignado que en este caso es 1
    print(f'r={r}')#Pasa lo mismo con esta variable pero se le asigna el valor 0
except (ZeroDivisionError, TypeError) as e: #Une las dos excepciones una en caso de ser division por 0 imprime la excepcion ZeroDivisonError y si es un valor str es decir caracteres imprime la excepcion TypeError
    print(type(e), e)#Se imprimen las dos excepciones pero si ocurre una sola se ejecuta una sola