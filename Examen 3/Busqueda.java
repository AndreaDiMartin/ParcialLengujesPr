//Andrea Diaz 18-10826
//Pregunta 1.c)

import java.util.*;

//Clase Grafo para las listas de adyacencia
class Grafo {
    ArrayList<ArrayList<Integer>> listaDeAdyacencia = new ArrayList<ArrayList<Integer>>();

    // Constructor de la clase que inicializa la lista de adyacencia con la cantidad
    // de nodos dada
    public Grafo(int n) {
        for (int i = 0; i < n; i++) {
            listaDeAdyacencia.add(new ArrayList<Integer>());
        }
    }

    // Metodo para agregar nodos en el grafo
    public void agregarNodo(int a, int b) {
        listaDeAdyacencia.get(a).add(b);
    }
}

// Clase abstracta Busqueda
abstract class Busqueda {
    public abstract int buscar(Grafo g, int D, int H);
}

// Clase DFS que hereda de Busqueda que recibe un grafo y dos nodos y devuelve
// la cantidad de nodos visitados
// Para ello se utiliza una pila para almacenar los nodos hijos de los que se
// van visitando
class DFS extends Busqueda {
    public int buscar(Grafo g, int D, int H) {
        ArrayList<Integer> visitados = new ArrayList<Integer>();
        Stack<Integer> pila = new Stack<Integer>();
        pila.push(D);
        while (!pila.empty()) {
            int actual = pila.pop();
            if (actual == H) {
                return visitados.size();
            }
            if (!visitados.contains(actual)) {
                visitados.add(actual);
                for (int i = 0; i < g.listaDeAdyacencia.get(actual).size(); i++) {
                    pila.push(g.listaDeAdyacencia.get(actual).get(i));
                }
            }
        }
        return -1;

    }
}

// Clase BFS que hereda de Busqueda que recibe un grafo y dos nodos y devuelve
// la cantidad de nodos visitados
// Para ello se utiliza una cola para almacenar los nodos hijos de los que se
// van visitando
class BFS extends Busqueda {
    public int buscar(Grafo g, int D, int H) {
        ArrayList<Integer> visitados = new ArrayList<Integer>();
        Queue<Integer> cola = new LinkedList<Integer>();
        cola.add(D);
        while (!cola.isEmpty()) {
            int actual = cola.remove();
            if (actual == H)
                return visitados.size();
            if (!visitados.contains(actual)) {
                visitados.add(actual);
                for (int i = 0; i < g.listaDeAdyacencia.get(actual).size(); i++) {
                    cola.add(g.listaDeAdyacencia.get(actual).get(i));
                }
            }
        }
        return -1;
    }
}
