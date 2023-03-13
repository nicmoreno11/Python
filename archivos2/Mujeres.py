import csv
with open('c:\\Users\\APRENDIZ\\Desktop\\repositorio\\Python\\archivos2\\oscar_age_female.csv')as oscar_muejeres:
    ganadores=csv.reader(oscar_muejeres)
    print(ganadores)
    for i in ganadores:
        print(i)
        print('Index:',i[0])
        print('Year:',i[1])
        print('Age:',i[2])
        print('Name:',i[3])
        print('Movie:',i[4])
