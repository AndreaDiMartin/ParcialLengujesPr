#Andrea Diaz 18-10826
#Examen 2
#Pregunta 2
#Programa creado para realizar las pruebas unitarias

def mostrar(orden, entrada):
    numeros = []
    operaciones = []
    anterior = '*'
    if orden == 'PRE':
        for i in entrada:
            if i.isdigit():
                numeros.append(int(i))
                anterior = i
            elif i != ' ':
                if(anterior.isdigit()):
                    numeros.append("stop")
                operaciones.append(i)
                anterior = i
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
        anterior = '9'
        for i in entrada:
            if i.isdigit():
                if(not(anterior.isdigit())):
                    numeros.append("stop")
                numeros.append(int(i))
                anterior = i
            elif i != ' ':
                operaciones.append(i)
                anterior = i
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

def eval(orden, entrada):
    numeros = []
    operaciones = []
    if orden == 'PRE':
        anterior = '*'
        for i in entrada:
            if i.isdigit():
                numeros.append(int(i))
                anterior = i
            elif i != ' ':
                if(anterior.isdigit()):
                    numeros.append("stop")
                operaciones.append(i)
                anterior = i
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
        anterior = '9'
        for i in entrada:
            if i.isdigit():
                if(not(anterior.isdigit())):
                    numeros.append("stop")
                numeros.append(int(i))
                anterior = i
            elif i != ' ':
                operaciones.append(i)
                anterior = i
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

