#Andreea Diaz
#Pregunta 3
#Para realizar tests
#Se modifica para realizar tests unitarios

import math
#Tomamos el input del usuario para el tamano de la memoria
#Funcion que verifica si hay dos bloques libres consecutivos y los une   
def rearrange():
    buddy = [['Libre',64],['Libre',32],['Libre',32],['Libre',16],['Libre',16],['Libre',16]]
    x = 0
    fr = 0
    while x in range(len(buddy)):
        if x!=0 and buddy[x][1] == buddy[x-1][1] and buddy[x][0] == 'Libre' and buddy[x-1][0] == 'Libre':
            buddy[x-1][1] = buddy[x][1] * 2
            buddy.pop(x) 
            x=1
            fr = fr+1
        else:
            x = x+1
    return fr
        
#Funcion que reserva un bloque de memoria de tamano a y con nombre name
def reservar(name,a):
    buddy = [['Libre',1024]]
    pos = -1
    i = -1
    #Verifica que no exista una direccion de memoria con el mismo nombre
    for x in range(len(buddy)):
        if buddy[x][0] == name:
            pass
    #Verifica si hay un bloque libre con el tamano necesario
    for x in range(len(buddy)):
        if buddy[x][0] == 'Libre' and a<=buddy[x][1]:
            i = x
            break
    #Si no lo hay, imprime un mensaje de error
    if i == -1:
        pass
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
            pos = i
            break
    return pos
    
    
#Funcion para liberar un bloque de memoria con nombre name
def liberar(name):
    buddy = [['A',64],['F',32],['Libre',32],['C',16],['Libre',16],['Libre',16]]
    lib = 0
    b = True
    for x in range(len(buddy)):
        if buddy[x][0] == name:
            b = False
            buddy[x][0] = 'Libre'
            lib = x
            break
    #Si no consigue un bloque con el nombre name, imprime un mensaje de error
    if(b):
        pass
    #De lo contrario se pasa a verificar si hay dos bloques libres consecutivos y los une
    else:
        rearrange()
    return lib
        