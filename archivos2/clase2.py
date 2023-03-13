from  clase import*
import csv
oscarMujer=[]
with open('c:\\Users\\APRENDIZ\\Desktop\\repositorio\\Python\\archivos2\\oscar_age_female.csv') as oscar_mujer:
    ganadores=csv.reader(oscar_mujer)
    for i in ganadores:
        ob=Actriz(i[0],i[1],i[2],i[3],i[4])
        oscarMujer.append(ob)
print(oscarMujer)
for actrices in oscarMujer:
    print(actrices.nombreCompleto())
print(oscarMujer[10])