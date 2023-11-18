#No empaquetado, se respeta la alineacion 
struct = [['meta2',['int', 'char']],['meta',['uni', 'bool','double']]]
union = [['uni',['int', 'char', 'bool']]]
atomico = [['int', '4', '4'], ['char', '1', '2'], ['bool', '1', '2'], ['double', '8', '8']]
printLine = []
values = range(0,40)
manejador = list(values)

def encontrarTipo(nombre):
    for i in struct:
        if(i[0] == nombre):
            return i, "struct"
    for i in union:
        if(i[0] == nombre):
            return i, "union"
    for i in atomico:
        if(i[0] == nombre):
            return i, "atomico"
    return "No existe", "No existe"

apuntador = 0
def describir(nombre, imprimir = True):
    #print(nombre)
    datos, tipoDescribir = encontrarTipo(nombre)
    if(datos == "No existe"):
        #print(nombre + " no existe")
        return 0,0
    tamaño = 0
    global apuntador
    desperdicio = 0
    #print(datos)
    #print(datos[1:])
    if(tipoDescribir == "atomico"):
        tipoNombre = datos[0]
        bytes = int(datos[1])
        tamaño = tamaño + bytes
        alineacion = int(datos[2])
        printLine.append(tipoNombre + ": Alineación " + str(alineacion))
        for j in range(apuntador,len(manejador)):
            if(j%alineacion == 0 and manejador[j] == j):
                apuntador = j+bytes
                for k in range(0,bytes):
                    manejador[j+k] = tipoNombre
                break
            else:
                desperdicio = desperdicio + 1
    if(tipoDescribir == "struct"):
        for i in datos[1:][0]:
            #print(i)
            datosTipo, tipo = encontrarTipo(i)
            if(tipo == "atomico"):
                tipoNombre = datosTipo[0]
                bytes = int(datosTipo[1])
                tamaño = tamaño + bytes
                alineacion = int(datosTipo[2])
                printLine.append(tipoNombre + ": Alineación " + str(alineacion))
                for j in range(apuntador,len(manejador)):
                    if(j%alineacion == 0 and manejador[j] == j):
                        apuntador = j+bytes
                        for k in range(0,bytes):
                            manejador[j+k] = tipoNombre
                        break
                    elif(j%alineacion != 0 and manejador[j] == j):
                        #print(j,apuntador, desperdicio, imprimir)
                        desperdicio = desperdicio + 1
            else:
                #print(apuntador)
                tamañoAux,desperdicioAux = describir(i,False) 
                tamaño = tamaño + tamañoAux
                desperdicio = desperdicio + desperdicioAux
                #print(desperdicio, imprimir)
                #print(apuntador)
    if(tipoDescribir == "union"):
        for i in datos[1:][0]:
            #print(i)
            datosTipo, tipo = encontrarTipo(i)
            manejadorAux = manejador.copy()
            desperdicioUnion = desperdicio
            apuntadores = []
            apuntadorAux = apuntador
            desperdicios = []
            if(tipo == "atomico"):
                tipoNombre = datosTipo[0]
                bytes = int(datosTipo[1])
                if(bytes > tamaño):
                    tamaño = bytes
                alineacion = int(datosTipo[2])
                printLine.append(tipoNombre + ": Alineación " + str(alineacion))
                for j in range(apuntadorAux,len(manejadorAux)):
                    if(j%alineacion == 0 and manejadorAux[j] == j):
                        apuntadorAux = j+bytes
                        for k in range(0,bytes):
                            manejadorAux[j+k] = tipoNombre
                        break
                    elif(j%alineacion != 0 and manejadorAux[j] == j):
                        #print(j,apuntador, desperdicio, imprimir)
                        desperdicioUnion = desperdicioUnion + 1
            else:
                #print(apuntador)
                tamañoAux,desperdicioAux = describir(i,False) 
                if(tamañoAux > tamaño):
                    tamaño = tamañoAux
                desperdicioUnion = desperdicio + desperdicioAux
            apuntadores.append(apuntadorAux)
            desperdicios.append(desperdicioUnion)
        apuntador = max(apuntadores)
        desperdicio = max(desperdicios)
    if(imprimir):
        #print(nombre + " :")
        #print("tamaño = " + str(tamaño+desperdicio) + " bytes")
        #for i in printLine:
        #    print(i + " bytes")
        #print("desperdicio = " + str(desperdicio) + " bytes")
        #print(manejador)
        return tamaño+desperdicio,desperdicio
    else:
        return tamaño+desperdicio, desperdicio

#print(describir('int'))
#print(describir('meta2'))
#print(describir('meta'))
#print(describir('uni'))
#print(manejador)
            