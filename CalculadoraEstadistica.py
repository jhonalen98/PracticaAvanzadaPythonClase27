# from collections import Counter

# # Función para pedir una lista de números
# def pedir_numeros():
#     numeros = []
#     while True:
#         entrada = input("Ingresa un número (o escribe 'fin' para terminar): ")
#         if entrada.lower() == 'fin':
#             break
#         try:
#             numero = float(entrada)
#             numeros.append(numero)
#         except ValueError:
#             print("Por favor, ingresa un número válido.")
#     return numeros

# # Función para calcular el promedio
# def calcular_promedio(numeros):
#     return sum(numeros) / len(numeros)

# # Función para calcular la mediana
# def calcular_mediana(numeros):
#     numeros_ordenados = sorted(numeros)
#     n = len(numeros_ordenados)
#     if n % 2 == 0:
#         mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
#     else:
#         mediana = numeros_ordenados[n//2]
#     return mediana

# # Función para calcular la moda
# def calcular_moda(numeros):
#     frecuencia = Counter(numeros)
#     moda = frecuencia.most_common(1)[0][0]
#     return moda

# # Función para calcular el rango
# def calcular_rango(numeros):
#     return max(numeros) - min(numeros)

# # Función principal
# def main():
#     numeros = pedir_numeros()
#     if len(numeros) == 0:
#         print("No se ingresaron números.")
#         return
    
#     promedio = calcular_promedio(numeros)
#     mediana = calcular_mediana(numeros)
#     moda = calcular_moda(numeros)
#     rango = calcular_rango(numeros)
    
#     print(f"Promedio: {promedio}")
#     print(f"Mediana: {mediana}")
#     print(f"Moda: {moda}")
#     print(f"Rango: {rango}")

# # Llamamos a la función principal
# main()

from collections import Counter
import math

# Función para pedir una lista de números
def pedir_numeros():
    numeros = []
    while True:
        entrada = input("Ingresa un número (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return numeros

# Función para calcular el promedio
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Función para calcular la mediana
def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        mediana = numeros_ordenados[n//2]
    return mediana

# Función para calcular la moda
def calcular_moda(numeros):
    frecuencia = Counter(numeros)
    moda = frecuencia.most_common(1)[0][0]
    return moda

# Función para calcular el rango
def calcular_rango(numeros):
    return max(numeros) - min(numeros)

# Funciones para calcular varianza y desviacion estandar (TAREA)
def calcular_varianza(numeros, promedio):
    varianza = sum((x - promedio) ** 2 for x in numeros) / len(numeros)
    return varianza

def calcular_desviacion_estandar(varianza):
    return math.sqrt(varianza)

# Función principal
def main():
    numeros = pedir_numeros()
    if len(numeros) == 0:
        print("No se ingresaron números.")
        return
    
    promedio = calcular_promedio(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    rango = calcular_rango(numeros)
    varianza = calcular_varianza(numeros, promedio)
    desviacion_estandar = calcular_desviacion_estandar(varianza)
    
    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Rango: {rango}")
    print(f"Varianza: {varianza}")
    print(f"Desviación Estándar: {desviacion_estandar}")

# Llamamos a la función principal
main()