import csv #Importa el archivo csv
header=['Fruit','Price'] #Se crea una lista con el nombre de header y con sus nombres ´fruit' y 'price'
rows=[['Apple',1200], #se crea una lista dentro de una lista con lo datos ya agregados
      ['Berry',2000], #se nombran los objetos y se les da un precio
      ['Lemon',1000], #se nombran los objetos y se les da un precio
      ['Melon',3000], #se nombran los objetos y se les da un precio
      ['Grapes',4000], #se nombran los objetos y se les da un precio
      ['Pear',2000]] #se nombran los objetos y se les da un precio

with open ('archivos/example.csv','w') as csvfile: #se abre el archivo y se le da el nombbre del directorio donde esta dicho archivo y si el archivo no existe como en este caso lo va a crear
    csvwriter=csv.writer(csvfile) #creamos una varibale y ponemos el nombre del archivo con el metodo write para poder escribir en el archivo
    csvwriter.writerow(header) #se crea la variable y se instacia con header para poder escribir en la columna
    csvwriter.writerows(rows) #se crea la variable y se instacia con rows para poder escribir en la fila