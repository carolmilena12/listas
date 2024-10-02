from lista_simple import ListaSimple

def eliminar_comunes(lista1, lista2):
    if lista1.esta_vacia() or lista2.esta_vacia():
        print("Una o ambas listas están vacías.")
        return None

    actual1 = lista1.p  # Nodo actual en lista1

    while actual1:  # Iteramos sobre la primera lista
        valor = actual1.valor  # Valor a buscar en lista2
        actual2 = lista2.p  # Nodo actual en lista2
        anterior2 = None  # Nodo anterior en lista2

        while actual2:  # Iteramos sobre la segunda lista
            if actual2.valor == valor:  # Si encontramos coincidencia
                if anterior2:  # Si no es el primer nodo
                    anterior2.siguiente = actual2.siguiente
                else:  # Si es el primer nodo
                    lista2.p = actual2.siguiente  # Actualizamos la cabeza de la lista
                break  # Salimos del bucle interno después de eliminar
            anterior2 = actual2  # Movemos el anterior
            actual2 = actual2.siguiente  # Avanzamos en lista2
        
        actual1 = actual1.siguiente  # Avanzamos en lista1

