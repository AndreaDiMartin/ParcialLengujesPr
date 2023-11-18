#Andrea Diaz
#18-10826
#Pregunta 5.1
#No empaquetado, se respeta la alineacion, la memoria tiene 40 bytes
struct = []
union = []
atomico = []
printLine = []
values = range(0,40)
manejador = list(values)

#Funcion que verifica si el tipos atomicos existen
def existeTipoAtomico(lista):
    flag = []
    for i in lista:
        for j in atomico:
            if(i == j[0]):
                flag.append(True)
    if(len(flag) == len(lista)):
        return True
    else:
        return False

#Funcion que verifica si el tipo existe
def noExisteTipo(nombre):
        for i in struct:
            if(i[0] == nombre):
                return False
        for i in union:
            if(i[0] == nombre):
                return False
        for i in atomico:
            if(i[0] == nombre):
                return False
        return True

#Funcion que encuentra y devuleve el tipo
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

#Funcion que guarda un tipo atomico
def guardarAtomico(nombre,representacion,alineacion):
    if(not(noExisteTipo(nombre))):
        print(nombre + " ya existe")
    else:
        atomico.append([nombre,representacion,alineacion])

#Funcion que guarda un tipo struct
def guardarStruct(nombre,tipo):
    if(not(noExisteTipo(nombre))):
        print(nombre + " ya existe")
    else:
        struct.append([nombre,tipo])

#Funcion que guarda un tipo union
def guardarUnion(nombre,tipo):
    if(not(noExisteTipo(nombre))):
        print(nombre + " ya existe")
    else:
        union.append([nombre,tipo])

#variable que apunta al siguiente lugar disponible
apuntador = 0

#Funcion que inserta un tipo en la memoria e imprime su tamano, alineacion y desperdicio
def describir(nombre, imprimir = True):
    datos, tipoDescribir = encontrarTipo(nombre)
    #Si el tipo no existe, se imprime un mensaje y se devuelve 0,0,0
    if(datos == "No existe"):
        print(nombre + " no existe")
        return 0,0,0
    tamaño = 0
    global apuntador
    desperdicio = 0
    #Si el tipo es atomico, se imprime se guarda directamente en la memoria, tomando en cuenta su alineacion
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
    #Si el tipo es struct, se imprime se revisa recursivamente los tipos que contiene, tomando en cuenta su alineacion
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
                    if(j%alineacion == 0 and manejador[j] == j):
                        apuntador = j+bytes
                        for k in range(0,bytes):
                            manejador[j+k] = tipoNombre
                        break
                    elif(j%alineacion != 0 and manejador[j] == j):
                        desperdicio = desperdicio + 1
            else:
                tamañoAux,desperdicioAux = describir(i,False) 
                tamaño = tamaño + tamañoAux
                desperdicio = desperdicio + desperdicioAux
    #Si el tipo es una union, se hace lo mismo que en un struct pero se guarda el mayor desperdicio y el mayor tamano y apuntador
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
                    if(j%alineacion == 0 and manejadorAux[j] == j):
                        apuntadorAux = j+bytes
                        for k in range(0,bytes):
                            manejadorAux[j+k] = tipoNombre
                        break
                    elif(j%alineacion != 0 and manejadorAux[j] == j):
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
    if(imprimir):
        print(nombre + " :")
        print("tamaño = " + str(tamaño+desperdicio) + " bytes")
        for i in printLine:
            print(i + " bytes")
        print("desperdicio = " + str(desperdicio) + " bytes")
        printLine.clear()
        print(manejador)
    else:
        return tamaño+desperdicio, desperdicio
                
#Loop para ingresar los comandos
while(True):
    entrada = input("Ingrese ATOMICO, STRUCT, UNION, DESCRIBIR o SALIR: ")
    if(entrada == "SALIR"):
        break
    elif(entrada[0:7] == "ATOMICO"):
        lista = entrada[8:].split(" ")
        nombre = lista[0]
        representacion = lista[1]
        alineacion = lista[2]
        guardarAtomico(nombre,representacion,alineacion)
    elif(entrada[0:6] == "STRUCT"):
        lista = entrada[7:].split(" ")
        nombre = lista[0]
        tipo = lista[1:]
        if(existeTipoAtomico(tipo)):
            guardarStruct(nombre,tipo)
        else:
            print("No existe uno de los tipos atomicos definidos")
    elif(entrada[0:5] == "UNION"):
        lista = entrada[6:].split(" ")
        nombre = lista[0]
        tipo = lista[1:]
        if(existeTipoAtomico(tipo)):
            guardarUnion(nombre,tipo)
        else:
            print("No existe uno de los tipos atomicos definidos")
    elif(entrada[0:9] == "DESCRIBIR"):
        lista = entrada[10:].split(" ")
        nombre = lista[0]
        describir(nombre)
    else:
        print("No es una entrada valida")


