#Andrea Diaz 18-10826
#Pregunta 6
#La funcion ASK  o que resuelve una regla no esta terminada

from itertools import chain
reglas = []
hechos = []

#Funcion que crea un predicado a partir de un string
def separador(str):
    lista = []
    aux = ""
    for i in str:
        if(i == " " and aux[-1] == ")"):
            lista.append(aux)
            aux = ""
        else:
            aux += i
    lista.append(aux)
    return lista

#Funcion que separa un predicado en una lista de strings
def separadorPredicado(str):
    lista = []
    aux = ""
    for i in str:
        if(i == "(" or i == "," or i == ")"):
            lista.append(aux)
            aux = ""
        elif(i == " "):
            pass
        else:
            aux += i
    if(aux != ""):
        lista.append(aux)
    return lista

#Funcion que separa una lista de listas en una lista
def separadorLista(lis):
    li = []
    if(len(lis)==1):
        return separadorLista(list(chain.from_iterable(lis)))
    else:
        for i in lis:
            if(type(i) == list):
                return separadorLista(list(chain.from_iterable(i)))
            elif(i == None):
                lis.remove(i)
            else:
                li.append(lis)
    return li

#Funcion que verifica si un hecho especifico es True o False
def verificadorHechoEspecifico(args,hecho):
    existe = True
    for i in args:
        if(i != hecho[args.index(i)]):
            existe = False
    return existe

#Funcion que genera respuestas correctas para un predicado con variables
def verificadorHechoGenerador(args,hecho):
    var = []
    valid = True
    result = []
    for i in args:
        if(i.isupper()):
            var.append(i)
    for i in args:
        if(i in var):
            pass
        else:
            if(i != hecho[args.index(i)]):
                valid = False
    print("hey")
    if(valid):
        for i in args:
            if(i in var):
                print(i," = ", hecho[args.index(i)])
                result.append([i,hecho[args.index(i)]])
    if(result != []):
        return result
    else:
        return None
            
            
#Funcion que averigua si se requiere comprar un hecho o generar una respuesta
def verificadorHecho(args,hecho):
    for i in args:
        if(i[0].isupper()):
           return verificadorHechoGenerador(args,hecho)
    return verificadorHechoEspecifico(args,hecho)
    
            
#Funcion que busca un hecho
def buscarHecho(lista):
    result = []
    for i in hechos:
        if(i[0] == lista[0]):
            result.append(verificadorHecho(lista[1:],i[1:]))
    if(result != []):
        return result
    else:
        return None

#Funcion que reemplaza las variables de una regla por los valores de un hecho
def reemplazarVar(regla,listaVar):
    newRegla = []
    newRegla.append([regla[0][0]])
    for i in range(1,len(listaVar)):
        newRegla[0].append(listaVar[i])
    for i in range(len(regla[1:])):
        newRegla.append([regla[i+1][0]])
        for j in range(len(regla[i][1:])):
            if(regla[i+1][j+1] in regla[0]):
                newRegla[i+1].append(listaVar[regla[0].index(regla[i+1][j+1])] )
            else:
                newRegla[i+1].append(regla[i+1][j+1])
                
    return newRegla


#Funcion que busca una regla
def buscarRegla(regla):
    lista = separadorPredicado(regla)
    for i in reglas:
        if(i[0][0] == lista[0]):
            copia = reemplazarVar(i,lista)
            result = []
            for j in copia[1:]:
               result.append(buscarHecho(j))
            print(result)

#Ciclo principal del programa para tomar entradas
while(True):
    entrada = input("Ingrese una accion a realizar: ")
    if(entrada[0:3] == "DEF"):
        if(entrada[4].islower()):
            lista = separador(entrada[4:])
            if(len(lista) > 1):
                regla = []
                for i in lista:
                    predicados = separadorPredicado(i)
                    if(predicados[0][0].isupper()):
                        raise "Error: El nombre de un predicado debe iniciar con minuscula"
                    else:
                        regla.append(predicados)
                reglas.append(regla)
                print("Se definio la regla:",entrada[4:])
            else:
                predicados = separadorPredicado(lista[0])
                if(predicados[0][0].isupper()):
                    print("Error: El nombre de un predicado debe iniciar con minuscula")
                else:
                    hechos.append(separadorPredicado(lista[0]))
                print("Se definio el hecho:",entrada[4:])
        else:
            print("Error: El nombre de un predicado debe iniciar con minuscula")
    elif(entrada[0:3] == "ASK"):
        buscarRegla(entrada[4:])
    elif(entrada[0:5] == "SALIR"):
        break
    else:
        print("Entrada no valida")