#Andrea Díaz 18-10826
#4)

from timeit import default_timer as timer
import matplotlib.pyplot as plt

alpha = ((8+2) % 5) +3
beta = ((2+6)%5) +3
#print(alpha) #3
#print(beta)  #6

#a) Formula recursiva
def formulaRecursiva(n):
    if n >=0  and n <18:
        return n
    else:
        return formulaRecursiva(n-6) + formulaRecursiva(n-12) + formulaRecursiva(n-18)

#b) Formula recursiva de cola
def formulaRecursivaColaAux(n,a,b,c,lista,contador):
    if contador == n+1:
        return a+b+c
    else:
        #Podemos ver que se utiliza una lógica similar a la formula iterativa
        a = lista[contador-6]
        b = lista[contador-12]
        c = lista[contador-18]
        lista[contador] = a+b+c
        return formulaRecursivaColaAux(n,a,b,c,lista,contador+1)

def formulaRecursivaCola(n):
    values = range(0,n+1)
    lista = list(values)
    if n >=0  and n <18:
        return n
    return formulaRecursivaColaAux(n,lista[18-6],lista[18-12],lista[18-18],lista, 18)


#c) Formula iterativa
#Con en el uso de una lista que simula la sucesión de valores de la formula recursiva, podemos acceder a valores anteriores con los que se
#calcula el valor actual
def formulaIterativa(n):
    values = range(0,n+1)
    lista = list(values)
    if(n <18 and n >=0):
        return lista[n]
    for i in range(18,n+1):
        lista[i] = lista[i-6] + lista[i-12] + lista[i-18] 
    return lista[n]

#Tomar tiempo
#Tiempo resultante de la ejecución de cada función para cada valor de entrada si se ejecuta el codigo comentado
listaValores = [50,100,200]
tiempoRecusivo = [9.299954399466515e-06, 0.0007877000607550144, 28.41495220013894]
tiempoIterativo = [5.100155249238014e-06, 9.699957445263863e-06, 1.9600149244070053e-05]
tiempoRecursivoCola = [1.019984483718872e-05, 4.2400090023875237e-05, 7.760012522339821e-05]

'''
for i in listaValores:
    start = timer()
    formulaRecursiva(i)
    end = timer()
    tiempoRecusivo.append(end-start)
    start = timer()
    formulaRecursivaCola(i)
    end = timer()
    tiempoRecursivoCola.append(end-start)
    start = timer()
    formulaIterativa(i)
    end = timer()
    tiempoIterativo.append(end-start)
'''

#Visualización de los resultados
#formulaRecursivaCola(1000)
plt.subplot(2,2,1)
plt.plot(listaValores,tiempoRecusivo, marker='o')
plt.title("Tiempo Recursivo")
plt.ylabel("Tiempo de Ejecución")
plt.xlabel("Tamaño de la Entrada")
#plt.ylim([9.299954399466515e-06, 29])
plt.subplot(2,2,2)
plt.plot(listaValores,tiempoIterativo, marker='o')
plt.title("Tiempo Iterativo")
plt.ylabel("Tiempo de Ejecución")
plt.xlabel("Tamaño de la Entrada")
#plt.ylim([9.299954399466515e-06, 29])
plt.subplot(2,2,3)
plt.plot(listaValores,tiempoRecursivoCola, marker='o')
plt.title("Tiempo Recursivo Cola")
plt.ylabel("Tiempo de Ejecución")
plt.xlabel("Tamaño de la Entrada")
#plt.ylim([9.299954399466515e-06, 29])
plt.show()


