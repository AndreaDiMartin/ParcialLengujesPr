#Andrea Diaz 
#Pregunta 5
#Se modifico TDiagram para realizar pruebas unitarias con unittest

programas = [['holamundo','LOCAL'], ['Buddy', 'wtf42'], ['Main', 'Java'], ['Fin','Ruby']]
interprete = [['C','LOCAL'],['C++','LOCAL']]
traductor = [['C','Java','C'],['C','wtf42','C++'],['A','Ruby','LOCAL']]

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


def ejecutar(programa):
    eje = False
    for i in programas:
        if i[0] == programa:
            return tombstone(i[1])
    print("No se encontro el programa " + programa)
    return eje    
    