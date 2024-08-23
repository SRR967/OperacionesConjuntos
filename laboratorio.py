import matplotlib.pyplot as plt
from matplotlib_venn import venn3


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


def graficar_interseccion(conjunto_a,conjunto_b,conjunto_c):
    set_a = set(conjunto_a)
    set_b = set(conjunto_b)
    set_c = set(conjunto_c)
    
    
    venn = venn3([set_a, set_b, set_c], ('Conjunto A', 'Conjunto B', 'Conjunto C'))

    
    unicos_a = set_a - set_b - set_c
    unicos_b = set_b - set_a - set_c
    unicos_c = set_c - set_a - set_b
    interseccion_abc = set_a & set_b & set_c

    
    if venn.get_label_by_id('100'):  
        venn.get_label_by_id('100').set_text('\n'.join(map(str, unicos_a)))
    if venn.get_label_by_id('010'):  
        venn.get_label_by_id('010').set_text('\n'.join(map(str, unicos_b)))
    if venn.get_label_by_id('001'):  
        venn.get_label_by_id('001').set_text('\n'.join(map(str, unicos_c)))
    if venn.get_label_by_id('111'):  
        venn.get_label_by_id('111').set_text('\n'.join(map(str, interseccion_abc)))

    plt.title("Diagrama de Venn para la Intersección de Conjuntos")
    plt.show()



def main ():
    conjuntos = ingresar_conjuntos()

    print("Unión: ", union(conjuntos))
    print("Intersección: ", interseccion(conjuntos))
    print("Diferencia del primer conjunto con respecto a los demás: ", diferencia(conjuntos[0], conjuntos[1:]))
    print("Diferencia simetrica de los dos primeros conjuntos: ", diferencia_simetrica(conjuntos[0],conjuntos[1]))
    print("¿El conjunto A es subconjunto B ?", es_subconjunto(conjuntos[0], conjuntos[1]))
    print("¿El conjunto A es superconjunto de B?", es_superconjunto(conjuntos[0],conjuntos[1]))



    
    #Se grafica la interseccion entre los dos primeros conjuntos
    graficar_interseccion(conjuntos[0], conjuntos[1], conjuntos[2])

main()

