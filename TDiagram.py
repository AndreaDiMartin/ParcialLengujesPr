#Andrea Diaz 
#Pregunta 5

#Declaramos listas para almacenar los programas, interpretes y traductores
programas = []
interprete = []
traductor = []

#Funcion recursiva que busca tanto en los traductores como en los interpretes si es posible llegar a un interprete local
#Se toma en cuenta que no se busque en el mismo traductor o interprete de donde se viene
#Se ve si el lenguaje destino y en el que esta escrito el traductor pueden conducir a LOCAL, si es asi da True
#Del resto se sigue buscando
def tombstone(lenguaje, postra = -1, postin = -1):
    if(lenguaje == "LOCAL"):
        return True
    else:
        for i in  range(0,len(traductor)):
            if traductor[i][1] == lenguaje and i != postra:
                if(tombstone(traductor[i][0],i,-1) and tombstone(traductor[i][2],i,-1)):
                   return True
                else:
                    pass
        for i in range(0,len(interprete)):    
            if interprete[i][0] == lenguaje and i != postin:
                if(tombstone(interprete[i][1],-1,i)):
                    return True
                else:
                    pass
    return False

#Llama a la funcion anterior y verifica si es posible ejecutar el programa
def ejecutar(programa):
    eje = False
    for i in programas:
        if i[0] == programa:
            return tombstone(i[1])
    print("No se encontro el programa " + programa)
    return eje    

#Se leen los comandos del usuario y se ejecutan las funciones correspondientes    
while True:
    res = input()
    if res[0:7] == 'DEFINIR':
        if(res[8:16] == 'PROGRAMA'):
             programas.append([res[17:].split(' ')[0],res[17:].split(' ')[1]])
             print("Se definio el programa " + res[17:].split(' ')[0] + ", ejecutable en " + res[17:].split(' ')[1])
        elif(res[8:18] == 'INTERPRETE'):
            interprete.append([res[19:].split(' ')[1],res[19:].split(' ')[0]])
            print("Se definio un interprete para " + res[19:].split(' ')[1] + ", escrito en " + res[19:].split(' ')[0])
        elif(res[8:17]== 'TRADUCTOR'):
            traductor.append([res[18:].split(' ')[0],res[18:].split(' ')[1],res[18:].split(' ')[2]])
            print("Se definio un traductor de " + res[18:].split(' ')[1] + " hacia " + res[18:].split(' ')[2] + ", escrito en " + res[18:].split(' ')[0])
        else:
            print("Los tipos a definir son PROGRAMA, INTERPRETE y TRADUCTOR")
    elif res[0:10] == 'EJECUTABLE':
        posible = ejecutar(res[11:])
        if(posible):
            print("Si, es posible ejecutar el programa " + res[11:])
        else:
            print("No es posible ejecutar el programa  " + res[11:])
    elif res[0:] == 'SALIR':
        break
    else:
        print("Los comandos a utilizar son DEFINIR, EJECUTABLE y SALIR")



