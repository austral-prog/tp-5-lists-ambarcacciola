# Ejercicio 6: Encontrar el mínimo en una lista

def find_min(lista):
    if lista != []:
        lista = min(lista)
        return lista
    else:
        return None
