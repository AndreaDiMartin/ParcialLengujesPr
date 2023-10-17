#Andreea Diaz
#Pregunta 3


import math
#Tomamos el input del usuario para el tamano de la memoria
n = input('Ingrese un valor para el tamaño inicial de la memoria: ')
#La memoria se representa por una lista de listas de la forma [nombre, tamano]
print(n)
buddy = [['Libre',int(n)]]

#Funcion que verifica si hay dos bloques libres consecutivos y los une   
def rearrange():
    x = 0
    while x in range(len(buddy)):
        if x!=0 and buddy[x][1] == buddy[x-1][1] and buddy[x][0] == 'Libre' and buddy[x-1][0] == 'Libre':
            buddy[x-1][1] = buddy[x][1] * 2
            buddy.pop(x) 
            x=1
        else:
            x = x+1
        
#Funcion que reserva un bloque de memoria de tamano a y con nombre name
def reservar(name,a):
    i = -1
    #Verifica que no exista una direccion de memoria con el mismo nombre
    for x in range(len(buddy)):
        if buddy[x][0] == name:
            print("YA EXISTE UNA DIRECCION DE MEMORIA CON ESE NOMBRE")
    #Verifica si hay un bloque libre con el tamano necesario
    for x in range(len(buddy)):
        if buddy[x][0] == 'Libre' and a<=buddy[x][1]:
            i = x
            break
    #Si no lo hay, imprime un mensaje de error
    if i == -1:
        print("NO HAY ESPACIO SUFICIENTE EN LA MEMORIA PARA SATISFACER SU PEDIDO")
    #Si lo hay, consigue el bloque de tamano mas cercano al tamano necesario y lo reserva. Si necesita dividirse, se le agrega 
    # una lista a buddy con el tamano dividido y el nombre 'Libre' y se reserva el bloque 
    for x in range(i+1,len(buddy)):
        if buddy[x][1] < buddy[i][1] and a<=buddy[x][1] and buddy[x][0] == 'F':
            i = x
    while(True):
        if buddy[i][1]//2 >= a:
            buddy[i][1] = buddy[i][1]//2
            if i<len(buddy)-1:
                buddy.insert(i+1, ['Libre',buddy[i][1]])
            elif i==len(buddy)-1:
                buddy.append(['Libre',buddy[i][1]])
        else:
            buddy[i][0] = name
            break
    
    
#Funcion para liberar un bloque de memoria con nombre name
def liberar(name):
    b = True
    for x in range(len(buddy)):
        if buddy[x][0] == name:
            b = False
            buddy[x][0] = 'Libre'
            break
    #Si no consigue un bloque con el nombre name, imprime un mensaje de error
    if(b):
        print('NO EXISTE UNA DIRECCION DE MEMORIA CON ESE NOMBRE')
    #De lo contrario se pasa a verificar si hay dos bloques libres consecutivos y los une
    else:
        rearrange()
        
     
#Imprime la memoria
def mostrar():
    pr = '|'
    for x in range(len(buddy)):
        pr = pr + buddy[x][0]
        pr = pr + ' : '
        pr = pr + str(buddy[x][1])
        pr = pr + ' '*int(math.log(buddy[x][1],2))
        pr = pr + '| '
    print(pr)

#Ciclo que permite al usuario ingresar los comandos
while(True):
    res = input("Ingrese una accion a realizar: ")
    print(res)
    if res[0:8] == 'RESERVAR':
        num = ''
        name =''
        for i in res[8:]:
            if i.isdigit():
                num +=i
            elif i != ' ':
                name += i
        reservar(name,int(num))
        
    elif res[0:7] == 'LIBERAR':
        name = ''
        for i in res[7:]:
            if i != ' ':
                name += i
        liberar(name)
    elif res[0:7] == 'MOSTRAR':
        mostrar()
    elif res[0:6] == 'SALIR':
        break
    else:
        print("Las palabras validad son RESERVAR , LIBERAR, MOSTRAR, SALIR")
    
