# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    lista_de_listas[0] = lista_de_listas[0][:2]
    lista_de_listas[1] = lista_de_listas[1][1:4]
    lista_de_listas[2] = lista_de_listas[2][-2:]
    return lista_de_listas
