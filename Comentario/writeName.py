import csv #se importa el nombre del archivo csv 
diccio=[ #se crea un diccionario
    {'name':'Alice','age':18}, #se crea un diccionario con sus respectivos datos
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]
header=['name','age'] # se crea una lista para que los datos queden guardados como filas
with open('archivos/people.csv','w') as csvfile: #se abre el archivo donde esta guardado y si no existe se crea uno nuevo
    writer=csv.DictWriter(csvfile,fieldnames=header) #
    writer.writeheader() #se llama el metod writeheader
    writer.writerows(diccio) #se llama el metodo y se instancia el diccionario