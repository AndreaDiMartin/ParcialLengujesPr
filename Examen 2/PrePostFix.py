#Andrea Diaz 18-10826
#Examen 2
#Pregunta 2

#Funcion para mostrar, dependiendo de si viene un * o un /, debido a la precedencia
#Se coloca entre parentesis segun sea el caso
def mostrar(orden, operaciones, numeros):
    if orden == "PRE":
        expr = ""
        a = numeros.pop(0)
        b = numeros.pop(0)
        op = operaciones.pop(0)
        flag = False
        if(operaciones[0]=="*" or operaciones[0]=="/"):
            expr = expr + "( " + str(a) + " "+ op + " " + str(b) + " )"
        else:
            expr = expr + str(a) + " " + op + " " + str(b)
        while(len(operaciones) > 0):
            a = numeros.pop(0)
            if(a == "stop"):
                flag =  True
                continue
            op = operaciones.pop(0)
            if(len(operaciones) > 0):
                if((operaciones[0]=="*" or operaciones[0]=="/") and not(flag)):
                    expr = "(" + expr
                    expr = expr + " " + op + " " + str(a) + " )"
                else:
                    expr = expr + " " + op + " " + str(a)   
            else:
                expr = expr + " " + op + " " + str(a)  
        return(expr)       
    else:
        flag  = False
        expr = ""
        a = numeros.pop(-1)
        b = numeros.pop(-1)
        op = operaciones.pop(-1)
        if(operaciones[-1]=="*" or operaciones[-1]=="/"):
            expr = "( " + str(a) + " "+ op + " " + str(b) + " )" + expr
        else:
            expr = str(a) + " " + op + " " + str(b) + expr
        while(len(operaciones) > 0):
            a = numeros.pop(-1)
            if(a == "stop" and flag == True):
                expr = "( "+ expr
                flag = False
            if(a == "stop" and (operaciones[-1] == "+" or operaciones[-1] == "-")):
                continue
            if(a == "stop" and (operaciones[-1] == "*" or operaciones[-1] == "/")):
                if(len(operaciones) > 1):
                    operaciones[-1] = ") " + operaciones[-1]
                    flag = True
                    continue
                else:
                    continue
            op = operaciones.pop(-1)
            if(len(operaciones) > 0):
                if(operaciones[-1]=="*" or operaciones[-1]=="/"):
                    expr = expr + ")" 
                    expr = "(" + " " + str(a) + " " +  op  + " "  + expr
                else:
                    expr =  str(a) + " " +  op + " " + expr
            else:
                expr =  str(a) + " " +  op  + " " + expr
        if(flag == True):
            expr = "( " + expr
        return(expr)    

#Funcion para evaluar la expresion, si es PRE se evalua la lista de izquierda a derecha, si es POST se hace lo contrario
#Se toman en cuenta los casos en que se trata de una expresion compuesta por otras subexpresiones
def eval(orden, operaciones, numeros):
    if orden == "PRE":
        i = 0
        while(len(operaciones) > 0):
            a = numeros.pop(0)
            b = numeros.pop(0)
            if b == "stop" or a == "stop":
                if a == "stop":
                    numeros.insert(len(numeros)-i,b)
                    i = i+1
                    continue
                else:
                    numeros.insert(len(numeros)-i,a)
                    i = i+1
                    continue
            op = operaciones.pop(0)
            if op == "+":
                numeros.insert(0,a+b)
            elif op == "-":
                numeros.insert(0,a-b)
            elif op == "*":
                numeros.insert(0,a*b)
            elif op == "/":
                numeros.insert(0,a//b)
        return numeros.pop(0)
    else:
        i = 0
        while(len(operaciones) > 0):
            a = numeros.pop(-1)
            b = numeros.pop(-1)
            op = operaciones.pop(-1)
            if b == "stop" or a == "stop":
                if a == "stop":
                    numeros.insert(0+i,b)
                    operaciones.insert(0+i,op)
                    i = i+1
                    continue
                else:
                    numeros.insert(0+i,a)
                    operaciones.insert(0+i,op)
                    i = i+1
                    continue
            if op == "+":
                numeros.insert(-1,a+b)
            elif op == "-":
                numeros.insert(-1,b-a)
            elif op == "*":
                numeros.insert(-1,b*a)
            elif op == "/":
                numeros.insert(-1,b//a)
        return numeros.pop(0)
    
#Loop para tomar la entrada, si se trata de una expresion con subexpresiones se coloca un 'stop' para
#saber cuando termina dicha subexpresion
while(True):
    entrada = input("Ingrese MOSTRAR, EVAL o SALIR: ")
    if(entrada[0:5] == "SALIR"):
        break
    elif(entrada[0:7] == "MOSTRAR"):
        if(entrada[8:11] == "PRE"):
            numeros = []
            operaciones = []
            anterior = '*'
            for i in entrada[9:]:
                if i.isdigit():
                    numeros.append(int(i))
                    anterior = i
                elif i != ' ':
                    if(anterior.isdigit()):
                        numeros.append("stop")
                    operaciones.append(i)
                    anterior = i
            print(mostrar("PRE",operaciones,numeros))
        elif(entrada[8:12] == "POST"):
            numeros = []
            operaciones = []
            anterior = '9'
            for i in entrada[12:]:
                if i.isdigit():
                    if(not(anterior.isdigit())):
                        numeros.append("stop")
                    numeros.append(int(i))
                    anterior = i
                elif i != ' ':
                    operaciones.append(i)
                    anterior = i
            print(mostrar("POST",operaciones,numeros))

    elif(entrada[0:4] == "EVAL"):
        if(entrada[5:8] == "PRE"):
            numeros = []
            operaciones = []
            anterior = '*'
            for i in entrada[9:]:
                if i.isdigit():
                    numeros.append(int(i))
                    anterior = i
                elif i != ' ':
                    if(anterior.isdigit()):
                        numeros.append("stop")
                    operaciones.append(i)
                    anterior = i
            print(eval("PRE",operaciones,numeros))
        elif(entrada[5:9] == "POST"):
            numeros = []
            operaciones = []
            anterior = '9'
            for i in entrada[10:]:
                if i.isdigit():
                    if(not(anterior.isdigit())):
                        numeros.append("stop")
                    numeros.append(int(i))
                    anterior = i
                elif i != ' ':
                    operaciones.append(i)
                    anterior = i
            print(eval("POST",operaciones,numeros))
    else:
        print("Comando no valido")
        continue