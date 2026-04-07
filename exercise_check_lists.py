# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    if len(lista1) > 2 and len(lista2) > 2:
        if lista1[2] == lista2[2]:
            return True
        else:
            return False
    else:
        return False
