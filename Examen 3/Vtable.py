#Andrea Diaz 18-10826
#Pregunta 4

Clases = []
visitados = []

#Funcion que busca ciclos en la jerarquia de clases, retorna True si hay ciclo
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

#Funcion que busca una clase en la lista de clases, retorna la clase si la encuentra
def buscarClase(nombre):
    for i in Clases:
        if i[0] == nombre:
            return i
    return None

#Funcion que busca metodos repetidos, retorna True si hay metodos repetidos
def metodoRepetido(metodo):
    for i in metodo:
        if metodo.count(i) > 1:
            return True
    return False

#Funcion que crea una clase a partir de su nombre, superclase y metodos, retorna el nombre de la clase si se crea
#Si una clase no tiene superclase se le asigna "superclase"
def crearClase(nombre,superclase,metodos):
    if buscarClase(nombre) != None:
        raise Exception("Clase ya definida")
    elif buscarCiclos(nombre,superclase):
        raise Exception("Ciclo en la jerarquia de clases")
    elif buscarClase(superclase) == None and superclase != "superclase":
        raise Exception("Superclase no definida")
    elif metodoRepetido(metodos):
        raise Exception("Existen metodos con nombres repetidos")
    else:
        Clases.append([nombre,superclase,metodos])
        return nombre

#Funcion que describe una clase a partir de su nombre, imprime en pantalla los metodos de la clase y sus padres
def describir(nombre):
    if buscarClase(nombre) != None:
        for i in buscarClase(nombre)[2]:
            if i not in visitados:
                visitados.append(i)
                print ( i + " -> " + nombre + " :: " + i)
        if buscarClase(nombre)[1] != "superclase":
            superclase = buscarClase(nombre)[1]
            describir(superclase)
        visitados.clear()
    else:
        raise Exception("Clase no definida")

#Funcion que recibe entradas por teclado y ejecuta las funciones correspondientes
while(True):
    entrada = input("Ingrese una accion a realizar: ")
    if entrada[0:5] == 'CLASS':
        lista = entrada[6:].split(" ")
        nombre = lista[0]
        if lista[1] == ":":
            superclase = lista[2]
            metodos = lista[3:]
        else:
            superclase = "superclase"
            metodos = lista[1:]
        crearClase(nombre,superclase,metodos)
    elif entrada[0:9] == 'DESCRIBIR':
        nombre = entrada[10:]
        describir(nombre)
    elif entrada[0:5] == "SALIR":
        break
    else:
        print("No es una entrada valida")
