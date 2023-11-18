#Para realizar test en ManTipoDatosNoAlin.py 
#La memoria tiene 40 bytes
#No empaquetado, no se respeta la alineacion 
struct = [['meta2',['int', 'char']],['meta',['int', 'char', 'bool', 'uni','double']]]
union = [['uni',['int', 'char', 'bool']]]
atomico = [['int', '4', '4'], ['char', '1', '2'], ['bool', '1', '2'], ['double', '8', '8']]
values = range(0,30)
printLine = []
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
    datos, tipoDescribir = encontrarTipo(nombre)
    if(datos == "No existe"):
        return 0,0
    global apuntador
    tamaño = 0
    desperdicio = 0
    if(tipoDescribir == "atomico"):
        tipoNombre = datos[0]
        bytes = int(datos[1])
        tamaño = tamaño + bytes
        alineacion = int(datos[2])
        printLine.append(tipoNombre + ": Alineación " + str(alineacion))
        for j in range(apuntador,len(manejador)):
            if(manejador[j] == j):
                apuntador = j+bytes
                for k in range(0,bytes):
                    manejador[j+k] = tipoNombre
                break
            else:
                desperdicio = desperdicio + 1
    if(tipoDescribir == "struct"):
        for i in datos[1:][0]:
            datosTipo, tipo = encontrarTipo(i)
            if(tipo == "atomico"):
                tipoNombre = datosTipo[0]
                bytes = int(datosTipo[1])
                tamaño = tamaño + bytes
                alineacion = int(datosTipo[2])
                printLine.append(tipoNombre + ": Alineación " + str(alineacion))
                for j in range(apuntador,len(manejador)):
                    if(manejador[j] == j):
                        apuntador = j+bytes
                        for k in range(0,bytes):
                            manejador[j+k] = tipoNombre
                        break
                    elif(manejador[j] == j):
                        desperdicio = desperdicio + 1
            else:
                tamañoAux,desperdicioAux = describir(i,False) 
                tamaño = tamaño + tamañoAux
                desperdicio = desperdicio + desperdicioAux
    if(tipoDescribir == "union"):
        for i in datos[1:][0]:
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
                    if(manejadorAux[j] == j):
                        apuntadorAux = j+bytes
                        for k in range(0,bytes):
                            manejadorAux[j+k] = tipoNombre
                        break
                    elif(manejadorAux[j] == j):
                        desperdicioUnion = desperdicioUnion + 1
            else:
                tamañoAux,desperdicioAux = describir(i,False) 
                if(tamañoAux > tamaño):
                    tamaño = tamañoAux
                desperdicioUnion = desperdicio + desperdicioAux
            apuntadores.append(apuntadorAux)
            desperdicios.append(desperdicioUnion)
        apuntador = max(apuntadores)
        desperdicio = max(desperdicios)
    return tamaño, desperdicio
