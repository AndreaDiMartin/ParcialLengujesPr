//Andrea Diaz 18-10826
//Pregunta 1.b)

//Interface Secuencia
interface Secuencia {
    Object[] elementos = new Object[100];

    void agregar(Object o);

    Object remover() throws Exception;

    boolean vacio();
}

// Clase para las pilas
class Pila implements Secuencia {
    int tope = 0;

    public void agregar(Object o) {
        elementos[tope++] = o;
    }

    public Object remover() throws Exception {
        if (vacio())
            throw new Exception("Pila vacia");
        return elementos[--tope];
    }

    public boolean vacio() {
        return tope == 0;
    }
}

// Clase para las colas
class Cola implements Secuencia {
    int inicio = 0;
    int fin = 0;

    public void agregar(Object o) {
        elementos[fin++] = o;
    }

    public Object remover() throws Exception {
        if (vacio())
            throw new Exception("Cola vacia");
        return elementos[inicio++];
    }

    public boolean vacio() {
        return inicio == fin;
    }
}
