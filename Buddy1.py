

import math

n = input('Ingrese un valor para el tamaño inicial de la memoria: ')
print(n)
buddy = [['Libre',int(n)]]
    
def rearrange():
    x = 0
    while x in range(len(buddy)):
        if x!=0 and buddy[x][1] == buddy[x-1][1] and buddy[x][0] == 'Libre' and buddy[x-1][0] == 'Libre':
            buddy[x-1][1] = buddy[x][1] * 2
            buddy.pop(x) 
            x=1
        else:
            x = x+1
        

def reservar(name,a):
    i = -1
    for x in range(len(buddy)):
        if buddy[x][0] == name:
            print("YA EXISTE UNA DIRECCION DE MEMORIA CON ESE NOMBRE")
    
    for x in range(len(buddy)):
        if buddy[x][0] == 'Libre' and a<=buddy[x][1]:
            i = x
            break
    if i == -1:
        print("NO HAY ESPACIO SUFICIENTE EN LA MEMORIA PARA SATISFACER SU PEDIDO")
        
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
    
    

def liberar(name):
    b = True
    for x in range(len(buddy)):
        if buddy[x][0] == name:
            b = False
            buddy[x][0] = 'Libre'
            break
    if(b):
        print('NO EXISTE UNA DIRECCION DE MEMORIA CON ESE NOMBRE')
    else:
        rearrange()
        
     

def mostrar():
    pr = '|'
    for x in range(len(buddy)):
        pr = pr + buddy[x][0]
        pr = pr + ' : '
        pr = pr + str(buddy[x][1])
        pr = pr + ' '*int(math.log(buddy[x][1],2))
        pr = pr + '| '
    print(pr)

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
    
        
#print(reservar('A',32))
#print(reservar('B',64))
#print(reservar('C',60))
#print(reservar('D',150))
#print(liberar('A'))
#print(liberar('B'))
#print(reservar('E',100))
#print(reservar('P',100))
#print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
#print('|' +  'A: 56          ' +  '|' + 'B: 256                     ' + '|         '                                                           '|')
#print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
#print(mostrar())