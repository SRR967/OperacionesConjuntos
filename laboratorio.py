def ingresar_conjuntos():
    num_conjuntos = int(input("¿Cuántos conjuntos desea ingresar? "))
    conjuntos = []
    for i in range(num_conjuntos):
        conjunto = input(f"Ingrese los elementos del conjunto {i + 1} separados por comas: ")
        conjuntos.append([int(x) for x in conjunto.split(",")])
    return conjuntos

def copiar_conjunto(A):
    copia = []
    for element in A:
        copia.append(element)
    return copia

def union(conjuntos):
    result = []
    for conjunto in conjuntos:
        for element in conjunto:
            if element not in result:
                result.append(element)
    return result

def interseccion(conjuntos):
    if not conjuntos:
        return []
    resultado = copiar_conjunto(conjuntos[0])

    for conjunto in conjuntos[1:]:
        nuevo_resultado = []
        for elemento in resultado:
            if elemento in conjunto:
                nuevo_resultado.append(elemento)
        resultado = nuevo_resultado
    return resultado

def diferencia(primer_conjunto, otros_conjuntos):
    resultado = copiar_conjunto(primer_conjunto)
    for conjunto in otros_conjuntos:
        nuevo_resultado = []    
        for elemento in resultado:
            if elemento not in conjunto:
                nuevo_resultado.append(elemento)
        resultado = nuevo_resultado
    
    return resultado

"""
def diferencia_simetrica(conjuntos):
    union_total = union(conjuntos)
    interseccion_total = interseccion(conjuntos)
    return diferencia(union_total, [interseccion_total])

"""

def diferencia_simetrica(conjunto_a, conjunto_b):
    diferencia_simetrica = set()
    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            diferencia_simetrica.add(elemento)
    for elemento in conjunto_b:
        if elemento not in conjunto_a:
            diferencia_simetrica.add(elemento)
    return diferencia_simetrica

def es_subconjunto(conjunto_A, otros_conjuntos):
    for conjunto_B in otros_conjuntos:
        for elemento in conjunto_A:
            if elemento not in conjunto_B:
                return False
    return True


def main ():
    conjuntos = ingresar_conjuntos()

    print("Unión: ", union(conjuntos))
    print("Intersección: ", interseccion(conjuntos))
    print("Diferencia del primer conjunto con respecto a los demás: ", diferencia(conjuntos[0], conjuntos[1:]))
    print("Diferencia simetrica de los dos primeros conjuntos: ", diferencia_simetrica(conjuntos[0],conjuntos[1]))

main()

