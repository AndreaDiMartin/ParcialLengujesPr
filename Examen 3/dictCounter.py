#Andrea Diaz 18-10826
#Pregunta 2.b.ii)

import threading
import os

#Ejemplo de ruta de prueba
rootPath = "c:/Users/andre/Documents/NetBeansProjects"
#En esta lista vacia se guardaran los resultados de cada hilo
results = []

#Funcion que cuenta los hilos
#Primero, se recorre la carpeta y se cuentan los archivos, luego se crea un hilo por cada carpeta que se encuentre
#y se repite el proceso hasta que no se encuentren mas carpetas y se unen los hilos
def countThreads(rootPath):
    count = 0
    for path in os.listdir(rootPath):
        if os.path.isfile(os.path.join(rootPath, path)):
            count += 1
        if os.path.isdir(os.path.join(rootPath,path)):
            x = threading.Thread(target=countThreads, args=(os.path.join(rootPath,path),))
            x.start()
            x.join()
    results.append(count)

#Funcion que suma los resultados de los hilos
def countFiles(rootPath):
    countThreads(rootPath)
    return sum(results)

#Se imprime el resultado (ejemplo)
print(countFiles(rootPath))