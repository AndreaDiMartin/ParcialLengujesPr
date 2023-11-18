//Andrea Diaz 18-10826
//1.b.ii)

import std.stdio;
import std.container : DList;

//Definicion de la clase Arbol
class Arbol {
    Arbol iz;
    int valor ;
    Arbol der;
    
    //Funcion para verificar si es simetrico
    
     bool esSimetrico(){
     //Primero verificamos que si es un arbol con un solo nodo, siempre sea true
      if((this.der is null)&& (this.iz is null)){
            return true;
      }
      //Creamos listas para guardar el preOrden y el postOrden
      //Ademas estas listas nos sirven para realizar los recorridos
      auto preOrder = DList!Arbol();
      auto preOrderValor = DList!int();
      auto postOrder = DList!Arbol();
      auto postOrderValor = DList!int();
      //Comenzamos insertando el valor del nodo actual en las listas que guardan el valor
      //Luego insertamos sus hijos en el las listas, verificando que ninguno sea null
      //En el caso del preOrder comenzamos del lado izquierdo, en el post order comenzamos del derecho
      preOrderValor.insertFront(this.valor);
      postOrderValor.insertFront(this.valor);
      if(!(this.der is null)){
            preOrder.insertBack(this.der);
            postOrder.insertFront(this.der);
        }
        if(!(this.iz is null)){    
            preOrder.insertFront(this.iz);
            postOrder.insertBack(this.iz);
        }
      //Recorrido PreOrden
      //Insertamos al inicio de las listas los valores y removemos tambien del principio
      while(!preOrder.empty){
        Arbol sim1 = preOrder.front();
        preOrder.removeFront();
        preOrderValor.insertBack(sim1.valor);
        if(!(sim1.der is null)){
            preOrder.insertFront(sim1.der);
        }
        if(!(sim1.iz is null)){    
            preOrder.insertFront(sim1.iz);
        }
      }
      //Recorrido PostOrden
      //Insertamos al inicio de las listas los valores y removemos tambien del principio
      //Sin embargo, insertamos los valores en al final
      while(!postOrder.empty){
        Arbol sim2 = postOrder.front();
        postOrder.removeFront();
        postOrderValor.insertFront(sim2.valor);
        if(!(sim2.iz is null)){
            postOrder.insertFront(sim2.iz);
        }
        if(!(sim2.der is null)){    
            postOrder.insertFront(sim2.der);
        }
      }
      //Verificamos que sea el mismo recorrido los primeros elementos
      while(!postOrderValor.empty){
         int x = postOrderValor.front(); 
         int y = preOrderValor.front();
         if(x!=y){
             return false;
         }
         postOrderValor.removeFront();
         preOrderValor.removeFront();
      }
      
      
      return true;
    }
    
    
    //Funcion para verficar que el arbol sea un max heap
    //Funcion recursiva que se mueve por los hijos de un nodo y verifica que su valor
    //siempre sea menor al de su padre
    bool esMaxHeap(){
        if((this.der is null)&& (this.iz is null)){
            return true;
        }
        else{
          if(!(this.iz is null)){
            if(this.iz.valor>this.valor){
              return false;
            }
            this.iz.esMaxHeap();
          }
          if(!(this.der is null)){
            if(this.der.valor> this.valor){
              return false;
            }
            this.der.esMaxHeap();
          }
        }
        return true;
    }
    //Verificar que el arbol es un max heap simetrico
    bool esMaxHeapSimetrico(){
        return this.esMaxHeap() && this.esSimetrico();
    }
}

void main(string[ ] args) {
    //Arbol de prueba 1
    Arbol rama1 =  new Arbol();
    rama1.valor = 11;
    Arbol rama2 = new Arbol();
    rama2.valor = 11;
    Arbol rama3 = new Arbol();
    rama3.valor = 11;
    Arbol hoja1 = new Arbol();
    hoja1.valor = 11;
    Arbol hoja2 = new Arbol();
    hoja2.valor = 11;
    Arbol hoja3 = new Arbol();
    hoja3.valor = 11;
    rama1.iz = rama2;
    rama1.der = rama3;
    rama2.iz = hoja3;
    rama2.der = hoja2;
    rama3.iz = hoja1;
    //Debe dar true
    writeln(rama1.esMaxHeapSimetrico());
    ////////////////////////////////////
    //Arbol de prueba 2
    Arbol raiz = new Arbol();
    raiz.valor = 9;
    Arbol rama11 = new Arbol();
    rama11.valor = 8;
    Arbol rama12 = new Arbol();
    rama12.valor = 8;
    Arbol hoja11 = new Arbol();
    hoja11.valor = 7;
    Arbol rama21 = new Arbol();
    rama21.valor = 6;
    Arbol hoja31 = new Arbol();
    hoja31.valor = 4;
    Arbol rama22 = new Arbol();
    rama22.valor = 6;
    Arbol hoja22 = new Arbol();
    hoja22.valor = 7;
    Arbol hoja33 = new Arbol();
    hoja33.valor = 4;
    raiz.iz = rama11;
    raiz.der = rama12;
    rama11.iz = hoja11;
    rama11.der = rama21;
    rama21.iz = hoja31;
    rama12.iz = rama22;
    rama12.der = hoja22;
    rama22.der = hoja33;
    //Debe dar true
    writeln(raiz.esMaxHeapSimetrico());
}