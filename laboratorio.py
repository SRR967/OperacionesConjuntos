import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from matplotlib_venn import venn2

"""
Abstraccion
Se solicita hacer operaciones basicas entre conjuntos y una representacion en diagrama de venn

Informacion relevante: Los conjuntos con que se realizarán las operaciones

Descomposicion: Que acciones se requieren

- Ingresar la imformación de cuantos conjuntos, y de los conjuntos
- Calcular la union, interseccion, diferencia, diferencia simetrica, 
    subconjuntos y superconjuntos de los conjuntos
- Generar el diagrama de venn
- Mostrar el diagrama
- Mostrar el mensaje

Reconocimiento de patrones
- ingresar_conjuntos
- copiar_conjuntos
- calcular_calcular_union
- calcular_calcular_interseccion
- calcular_calcular_diferencia
- calcular_calcular_diferencia_simetrica
- es_subconjuntos
- es_superconjuntos

"""

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

def calcular_union(conjuntos):
    result = []
    for conjunto in conjuntos:
        for element in conjunto:
            if element not in result:
                result.append(element)
    return result

def calcular_interseccion(conjuntos):
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

def calcular_diferencia(primer_conjunto, otros_conjuntos):
    resultado = copiar_conjunto(primer_conjunto)
    for conjunto in otros_conjuntos:
        nuevo_resultado = []    
        for elemento in resultado:
            if elemento not in conjunto:
                nuevo_resultado.append(elemento)
        resultado = nuevo_resultado
    
    return resultado


def calcular_diferencia_simetrica(conjunto_a, conjunto_b):
    calcular_diferencia_simetrica = set()
    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            calcular_diferencia_simetrica.add(elemento)
    for elemento in conjunto_b:
        if elemento not in conjunto_a:
            calcular_diferencia_simetrica.add(elemento)
    return calcular_diferencia_simetrica

def es_subconjunto(conjunto_A, conjunto_B):
    for elemento in conjunto_A:
        if elemento not in conjunto_B:
            return False
    return True


def es_superconjunto(conjunto_A, conjunto_B):
    es_superconjunto = True
    for elemento in conjunto_B:
        if elemento not in conjunto_A:
            es_superconjunto = False
            break
    return es_superconjunto

def graficar_interseccion_2(conjunto_a,conjunto_b):
    set_a = set(conjunto_a)
    set_b = set(conjunto_b)
    venn = venn2([set_a, set_b], ('Conjunto A', 'Conjunto B'))

    unicos_a = set_a - set_b
    unicos_b = set_b - set_a

    interseccion_ab = set_a & set_b

    if venn.get_label_by_id('10'):  
        venn.get_label_by_id('10').set_text('\n'.join(map(str, unicos_a)))
    if venn.get_label_by_id('01'):  
        venn.get_label_by_id('01').set_text('\n'.join(map(str, unicos_b)))
    if venn.get_label_by_id('11'):  
        venn.get_label_by_id('11').set_text('\n'.join(map(str, interseccion_ab)))

    plt.title("Diagrama de Venn para la Intersección de Conjuntos")
    plt.show()



def graficar_interseccion_3(conjunto_a,conjunto_b,conjunto_c):
    set_a = set(conjunto_a)
    set_b = set(conjunto_b)
    set_c = set(conjunto_c)

    # Crear el diagrama de Venn
    venn = venn3([set_a, set_b, set_c], ('Conjunto A', 'Conjunto B', 'Conjunto C'))

    # Elementos únicos de cada región
    unicos_a = set_a - set_b - set_c
    unicos_b = set_b - set_a - set_c
    unicos_c = set_c - set_a - set_b
    interseccion_ab = set_a & set_b - set_c
    interseccion_ac = set_a & set_c - set_b
    interseccion_bc = set_b & set_c - set_a
    interseccion_abc = set_a & set_b & set_c

    # Asignar los elementos a las etiquetas del diagrama de Venn
    if venn.get_label_by_id('100'):  
        venn.get_label_by_id('100').set_text('\n'.join(map(str, unicos_a)))
    if venn.get_label_by_id('010'):  
        venn.get_label_by_id('010').set_text('\n'.join(map(str, unicos_b)))
    if venn.get_label_by_id('001'):  
        venn.get_label_by_id('001').set_text('\n'.join(map(str, unicos_c)))
    if venn.get_label_by_id('110'):  
        venn.get_label_by_id('110').set_text('\n'.join(map(str, interseccion_ab)))
    if venn.get_label_by_id('101'):  
        venn.get_label_by_id('101').set_text('\n'.join(map(str, interseccion_ac)))
    if venn.get_label_by_id('011'):  
        venn.get_label_by_id('011').set_text('\n'.join(map(str, interseccion_bc)))
    if venn.get_label_by_id('111'):  
        venn.get_label_by_id('111').set_text('\n'.join(map(str, interseccion_abc)))

    # Título del gráfico
    plt.title("Diagrama de Venn para la Intersección de Conjuntos")
    plt.show()

def graficar_conjuntos(conjuntos):
    
    if len(conjuntos) == 2:
        graficar_interseccion_2(conjuntos[0],conjuntos[1])
    elif len(conjuntos) == 3:
        graficar_interseccion_3(conjuntos[0],conjuntos[1],conjuntos[2])
    else:
        print("No se puede graficar la interseccion de mas de 3 conjuntos")


def main ():
    conjuntos = ingresar_conjuntos()

    print("Unión: ", calcular_union(conjuntos))
    print("Intersección: ", calcular_interseccion(conjuntos))
    print("Diferencia del primer conjunto con respecto a los demás: ", calcular_diferencia(conjuntos[0], conjuntos[1:]))
    print("Diferencia simetrica de los dos primeros conjuntos: ", calcular_diferencia_simetrica(conjuntos[0],conjuntos[1]))
    print("¿El conjunto A es subconjunto B ?", es_subconjunto(conjuntos[0], conjuntos[1]))
    print("¿El conjunto A es superconjunto de B?", es_superconjunto(conjuntos[0],conjuntos[1]))
    
    #Se grafica la calcular_interseccion entre los tres primeros conjuntos
    graficar_conjuntos(conjuntos)

main()

