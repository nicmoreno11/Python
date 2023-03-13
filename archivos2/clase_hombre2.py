from  clase_hombre import*
import csv
oscarHombre=[]
with open('c:\\Users\\APRENDIZ\\Desktop\\repositorio\\Python\\archivos2\\oscar_age_female.csv') as oscar_hombre:
    ganadores=csv.reader(oscar_hombre)
    for i in ganadores:
        ob=Actor(i[0],i[1],i[2],i[3],i[4])
        oscarHombre.append(ob)
print(oscarHombre)
for actrices in oscarHombre:
    print(actrices.nombreCompleto())
print(oscarHombre[20])

