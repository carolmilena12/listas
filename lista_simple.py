# lista_simple.py

from nodo import Nodo  # Importamos la clase Nodo

class ListaSimple:
    def __init__(self):
        self.p = None
    
    def esta_vacia(self):
        return self.p is None
    
    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.p = nuevo_nodo
        else:
            actual = self.p
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.p
        self.p = nuevo_nodo
    
    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente  
        print("None")  # Indica el final de la lista

    def eliminar_final(self):
        if self.esta_vacia():
            print ("La lista no tiene nodos")
            return None
        elif self.p.siguiente is None:
            nodo_eliminado = self.p
            self.p=None
        else:
            actual = self.p
            while actual.siguiente:
                anterior = actual
                actual = actual.siguiente
            nodo_eliminado = anterior.siguiente
            anterior.siguiente = None
        return nodo_eliminado  

    def contar_nodos(self):
        actual = self.p
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador 
    
    def eliminar_inicio(self):
        if self.esta_vacia():
            print ("Lista esta vacia")
            return None
        else:
            nodo_eliminado = self.p
            self.p= self.p.siguiente
            return nodo_eliminado
        
