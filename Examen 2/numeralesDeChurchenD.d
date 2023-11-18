//Andrea Diaz 18-10826
//1.b.i)

import std.stdio;

//Union de los numerales de Church
union churchNumerales {
    int Cero = 0; 
    churchNumerales* Suc;
    
    //Funcion de suma
    
    int suma(churchNumerales* sumando){
        //Contador para ir contando los sucesores 
        int sumador = 0;
        churchNumerales aux = this;
        //Verificamos que no se trata de un Cero, si es un Cero seguimos buscando y sumamos sucesores hasta encontrar el Cero
        if(aux.Cero != 0){
            churchNumerales* sucesorAux = aux.Suc;
            sumador = sumador+1;
            while(sucesorAux.Cero != 0){
                sumador = sumador+1;
                sucesorAux = sucesorAux.Suc;
            }
        }
        //Repetimos el mismo proceso para el otro numeral de Church
        int sumador1 = 0;
        churchNumerales* sumandoAux = sumando;
        while(sumandoAux.Cero != 0){
            sumador1 = sumador1+1;
            sumandoAux = sumandoAux.Suc;
        }
        //Sumamos el resultado
        return sumador+sumador1;
        
    }
    //Funcion de multiplicacion
    int multiplicacion(churchNumerales* multiplicando){
        //Contador para ir contando los sucesores 
        int sumador = 0;
        churchNumerales aux = this;
        //Verificamos que no se trata de un Cero, si es un Cero seguimos buscando y sumamos sucesores hasta encontrar el Cero
        if(aux.Cero != 0){
            churchNumerales* sucesorAux = aux.Suc;
            sumador = sumador+1;
            while(sucesorAux.Cero != 0){
                sumador = sumador+1;
                sucesorAux = sucesorAux.Suc;
            }
        }
        //Repetimos el mismo proceso para el otro numeral de Church 
        int sumador1 = 0;
        churchNumerales* multAux = multiplicando;
        while(multAux.Cero != 0){
            sumador1 = sumador1+1;
            multAux = multAux.Suc;
        }
        //Multiplicamos los sucesores
        return sumador1*sumador;
        
    }
    
}

void main(string[ ] args) {
    churchNumerales* v = new churchNumerales();
    churchNumerales* c = new churchNumerales();
    churchNumerales* b = new churchNumerales();
    churchNumerales* n = new churchNumerales();
    c.Suc = v;
    b.Suc = c;
    int multiplicacion = b.multiplicacion(c); 
    int suma = c.suma(b);
    writeln(multiplicacion);
    writeln(suma);
}