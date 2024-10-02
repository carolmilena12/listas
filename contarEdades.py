from lista_simple import ListaSimple

def contarEdades(lista, edad):
    if lista.esta_vacia():  # Verifica si la lista está vacía
        print("La lista está vacía....")
        return 0  # Retorna 0 ya que no hay nodos

    actual = lista.p
    cont = 0
    while actual:
        if actual.valor == edad:
            cont += 1
        actual = actual.siguiente

    if cont == 0:  # Si no se encontró la edad
        print(f"No se encontraron coincidencias para la edad {edad}.")
    
    return cont


lista1 = ListaSimple()

lista1.agregar_final(18)
lista1.agregar_final(21)
lista1.agregar_final(18)
lista1.agregar_final(18)
lista1.agregar_final(19)
lista1.agregar_final(18)
lista1.agregar_final(22)
lista1.agregar_final(21)

edad = int(input("ingresar edad----> "))

edades = contarEdades(lista1,edad)
print(f"Número de coincidencias para la edad {edad}: {edades}")

