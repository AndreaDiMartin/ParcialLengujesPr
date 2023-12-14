#Andrea Diaz 18-10826
#Pregunta 4 
#Version para las pruebas

#Se predefinen las siguientes clases
Clases = [["A", "superclase", ["f","g"]], ["B", "A", ["f","h"]],["C","B",["f","h","g"]]]
visitados = []

def buscarCiclos(nombre,superclase):
    if nombre == superclase:
        return True
    else:
        for i in Clases:
            if i[0] == superclase:
                if i[1] == "superclase":
                    return False
                else:
                    return buscarCiclos(nombre,i[1])

def buscarClase(nombre):
    for i in Clases:
        if i[0] == nombre:
            return i
    return None

def metodoRepetido(metodo):
    for i in metodo:
        if metodo.count(i) > 1:
            return True
    return False

#Retorna false si no se pueden crear las clases
def crearClase(nombre,superclase,metodos):
    if buscarClase(nombre) != None:
        return False
    elif buscarClase(superclase) == None and superclase != "superclase":
        return False
    elif buscarCiclos(nombre,superclase):
        return False
    elif metodoRepetido(metodos):
        return False
    else:
        Clases.append([nombre,superclase,metodos])
        return True

res = []
#Retorna una lista con tuplas que contienen el metodo y su padre
def describir(nombre,head = True):
    if buscarClase(nombre) != None:
        for i in buscarClase(nombre)[2]:
            if i not in visitados:
                visitados.append(i)
                res.append((nombre, i))
        if buscarClase(nombre)[1] != "superclase":
            superclase = buscarClase(nombre)[1]
            describir(superclase, False)
        visitados.clear()
    else:
        raise Exception("Clase no definida")
    if head:
        ress = res.copy()
        res.clear()
        return ress
    return res

