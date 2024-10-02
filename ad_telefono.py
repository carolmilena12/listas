from lista_simple import ListaSimple
from nodo import Nodo

def ad_telefono(Lista, i,numero):
    nodo_nuevo = Nodo(numero)
    actual1 = Lista.p
    actual2 = Lista.p
    existe = False
    while actual1:
        if actual1.valor == numero:
            existe = True
            break
        actual1=actual1.siguiente
    if existe:
        print ("El numero de telefono ya existe")

    else:
        contador = 1
        while actual2 and contador<i:
            actual2=actual2.siguiente
            contador += 1
        if actual2 is None:
            print ("La posicion i es invalida")
        elif contador==i:
            nodo_nuevo.siguiente = actual2.siguiente
            actual2.siguiente = nodo_nuevo
            print ("El nummero de telefono ha sido añadido despues de la iesima posicion")
        else: 
            print ("La posicion i es invalida")

lista1 = ListaSimple()
lista1.agregar_inicio(123)
lista1.agregar_inicio(234)
lista1.agregar_final(345)

lista1.mostrar_lista()
ad_telefono(lista1,2,123)

lista1.mostrar_lista()



