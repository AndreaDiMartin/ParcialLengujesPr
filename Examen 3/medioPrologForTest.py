#Andrea Diaz 18-10826
#Pregunta 6
#medioProlog modificado para hacer tests

from itertools import chain
reglas = []
hechos = [["padre","juan","jose"]]

def crearPredicado(lis):
    if(lis[0].islower()):
            lista = separador(lis[4:])
            if(len(lista) > 1):
                regla = []
                for i in lista:
                    predicados = separadorPredicado(i)
                    if(predicados[0][0].isupper()):
                        return False
                    else:
                        regla.append(predicados)
                reglas.append(regla)
                return True
            else:
                predicados = separadorPredicado(lista[0])
                if(predicados[0][0].isupper()):
                    return False
                else:
                    hechos.append(separadorPredicado(lista[0]))
                return True
    else:
        return False

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

def verificadorHechoEspecifico(args,hecho):
    existe = True
    for i in args:
        if(i != hecho[args.index(i)]):
            existe = False
    return existe

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
    if(valid):
        for i in args:
            if(i in var):
                result.append([i,hecho[args.index(i)]])
    if(result != []):
        return result
    else:
        return None

def verificadorHecho(args,hecho):
    for i in args:
        if(i[0].isupper()):
           return verificadorHechoGenerador(args,hecho)
    return verificadorHechoEspecifico(args,hecho)
    
def buscarHecho(lista):
    for i in hechos:
        if(i[0] == lista[0]):
            return verificadorHecho(lista[1:],i[1:])
    else:
        return None

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

