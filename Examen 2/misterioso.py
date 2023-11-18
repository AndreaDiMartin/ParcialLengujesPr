#Andrea Díaz 18-10826
#2.b)

#Funcion que retorna los miembros del conjunto de las partes de un conjunto en orden creciente            
def misterio(p):
    if p == []:
        yield []
    else:
        for x in misterio(p[1:]):
            #Verifica que el conjunto este en orden creciente, de lo contrario no lo retorna
            test_list1 = x[:]
            test_list1.sort()
            if (test_list1 == x):
                yield x
                yield [p[0],*x]

for x in misterio([1,4,3,2,5]):
    print(x)
