from lista_simple import ListaSimple

def encontrar_comunes(lista1, lista2):
    if lista1.esta_vacia() or lista2.esta_vacia():
        print("Una o ambas de las listas esta vacia")
        return None

    comunes = []  # Lista para almacenar elementos en común
    actual1 = lista1.p

    while actual1:  # Iteramos sobre la primera lista
        actual2 = lista2.p
        while actual2:  # Iteramos sobre la segunda lista
            if actual1.valor == actual2.valor:  # Si hay coincidencia
                comunes.append(actual1.valor)
                break  # Salimos del bucle interno si encontramos una coincidencia
            actual2 = actual2.siguiente
        actual1 = actual1.siguiente

    return comunes

# Ejemplo de uso
if __name__ == "__main__":
    # Creación de las listas de ejemplo
    lista1 = ListaSimple()
    lista1.agregar_final(1)
    lista1.agregar_final(2)
    lista1.agregar_final(3)
    lista1.agregar_final(7)
    lista1.agregar_final(4)
    lista1.mostrar_lista()
    
    lista2 = ListaSimple()
    lista2.agregar_final(3)
    lista2.agregar_final(1)
    lista2.agregar_final(5)
    lista2.mostrar_lista()

    # Encontrar y mostrar elementos comunes
    comunes = encontrar_comunes(lista1, lista2)
    if comunes:
        print("Elementos en común:", comunes)
    else:
        print("No hay elementos en común.")