#Andrea Diaz 18-10826 
#Pregunta 4
# Modulo para realizar operaciones aritmeticas en vectores tridimensionales

import math

#La clase vector representa un vector tridimensional y define las operaciones de suma, resta, producto punto, producto cruz, norma.
class vector:
    #Constructor de la clase vector
    def __init__(self, a, b, c):
       self.v = (a,b,c)
    #Sobrecarga del operador de suma para sumar dos vectores o un vector y un escalar 
    def __add__(self, a):
        if type(a) == vector:
            return vector(self.v[0] + a.v[0],self.v[1] + a.v[1], self.v[2] + a.v[2])
        elif type(a) == float or type(a) == int:
            return vector(self.v[0] + a,self.v[1] + a, self.v[2] + a)
    #Sobrecarga del operador de resta para restar dos vectores o un vector y un escalar   
    def __sub__(self, a):
        if type(a) == vector:
            return vector(self.v[0] - a.v[0],self.v[1] - a.v[1], self.v[2] - a.v[2])
        elif type(a) == float or type(a) == int:
            return vector(self.v[0] - a,self.v[1] - a, self.v[2] - a) 
    #Sobrecarga del operador de producto punto multiplicar dos vectores
    def __mod__(self, other):
        return self.v[0] * other.v[0] + self.v[1] * other.v[1] + self.v[2] * other.v[2]
    #Sobercarga del operador de producto cruz para multiplicar dos vectores o un vector y un escalar
    def __mul__(self, a):
        if type(a) == vector: 
            i = self.v[1] * a.v[2] - self.v[2]*a.v[1]
            j = self.v[0] * a.v[2] - self.v[2]*a.v[0]
            k = self.v[0] * a.v[1] - self.v[1]*a.v[0]
            return vector(i, -j, k) 
        elif type(a) == float or type(a) == int:
            return vector(self.v[0] * a,self.v[1] * a, self.v[2] * a)
    #Sobrecarga del operador invert, no logre usar el &, por lo que se uso el ~ para calcular la norma de un vector    
    def __invert__(self):
        return math.sqrt(self.v[0]**2 + self.v[1]**2 + self.v[2]**2)
    #Sobrecarga del operador de impresion para imprimir el vector
    def __str__(self):
        return "(" + ", ".join(map(str,self.v)) + ")"
