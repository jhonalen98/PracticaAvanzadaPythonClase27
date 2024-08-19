# import random

# # Variables globales
# intentos_max = 5
# numero_secreto = random.randint(1, 100)

# # Función para pedir una adivinanza
# def pedir_adivinanza():
#     try:
#         return int(input("Adivina el número (entre 1 y 100): "))
#     except ValueError:
#         print("Por favor, ingresa un número válido.")
#         return pedir_adivinanza()

# # Función principal del juego
# def juego_adivinanza():
#     intentos = 0
#     while intentos < intentos_max:  # Bucle while
#         adivinanza = pedir_adivinanza()
#         intentos += 1
        
#         if adivinanza < numero_secreto:  # Bifurcación doble
#             print("Demasiado bajo.")
#         elif adivinanza > numero_secreto:
#             print("Demasiado alto.")
#         else:
#             print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
#             break
#     else:
#         print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")

# # Función principal para iniciar el juego
# def main():
#     juego_adivinanza()

# # Llamamos a la función principal
# main()

import random

# Variables globales modificadas para permitirle al usuario el ingreso de intentos y rango (TAREA)
intentos_max = int(input("Ingrese el numero de intentos que desea tener: "))
menor=int(input("Ingrese el rango inferior que desea adivinar: "))
mayor=int(input("Ingrese el rango superior que desea adivinar: "))

numero_secreto = random.randint(menor, mayor)

# Función para pedir una adivinanza
def pedir_adivinanza():
    try:
        return int(input(f"Adivina el número (entre {menor} y {mayor}): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return pedir_adivinanza()

# Función principal del juego
def juego_adivinanza():
    intentos = 0
    while intentos < intentos_max:  # Bucle while
        adivinanza = pedir_adivinanza()
        intentos += 1
        
        if adivinanza < numero_secreto:  # Bifurcación doble
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
    else:
        print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")

# Función principal para iniciar el juego
def main():
    juego_adivinanza()

# Llamamos a la función principal
main()