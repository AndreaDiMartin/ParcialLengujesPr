#Andrea Diaz 18-10826
#Pregunta 2.b.i)

import time
from concurrent import futures

#Vectores de prueba
A = [-3,5,4]
B = [2,-4,1]

#Se guardan los vectores en una lista
vectores = [A,B]


#Funcion que multiplica un elemento de cada vector y los suma
def calculoPP(a,b,result):
    result += a*b
    return result

#Funcion que crea un hilo por cada elemento de los vectores y llama a la funcion calculoPP
def productosPuntos(vectores):
  with futures.ThreadPoolExecutor(max_workers=2) as executor:
        result = 0
        for i in range(len(A)):
            future = executor.submit(calculoPP,A[i],B[i],result)
            result = future.result()
            time.sleep(1)
        print(result)
            

#Se imprime el resultado (ejemplo)
print(productosPuntos(vectores))

