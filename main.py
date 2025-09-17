#!/usr/bin/env python3
"""
Calculadora Modular
Menú principal para la calculadora con operaciones básicas y avanzadas.
"""

from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import sumar_varios


def mostrar_menu():
    """Muestra el menú de opciones disponibles."""
    print("\n" + "="*40)
    print("         CALCULADORA MODULAR")
    print("="*40)
    print("1. Sumar dos números")
    print("2. Restar dos números") 
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar varios números")
    print("6. Salir")
    print("="*40)


def obtener_numero(mensaje):
    """
    Obtiene un número del usuario con validación.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        float: El número ingresado por el usuario
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")


def obtener_varios_numeros():
    """
    Obtiene varios números del usuario.
    
    Returns:
        list: Lista de números ingresados por el usuario
    """
    numeros = []
    print("Ingrese los números (presione Enter sin escribir nada para terminar):")
    
    while True:
        try:
            entrada = input(f"Número {len(numeros) + 1}: ")
            if entrada.strip() == "":
                break
            numeros.append(float(entrada))
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    return numeros


def ejecutar_operacion_basica(operacion, nombre_operacion):
    """
    Ejecuta una operación básica con dos números.
    
    Args:
        operacion (function): Función de operación a ejecutar
        nombre_operacion (str): Nombre de la operación para mostrar
    """
    print(f"\n--- {nombre_operacion.upper()} ---")
    num1 = obtener_numero("Ingrese el primer número: ")
    num2 = obtener_numero("Ingrese el segundo número: ")
    
    try:
        resultado = operacion(num1, num2)
        print(f"Resultado: {num1} {'+' if nombre_operacion == 'suma' else '-' if nombre_operacion == 'resta' else '*' if nombre_operacion == 'multiplicación' else '/'} {num2} = {resultado}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


def main():
    """Función principal del programa."""
    print("¡Bienvenido a la Calculadora Modular!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            
            if opcion == 1:
                ejecutar_operacion_basica(sumar, "suma")
            
            elif opcion == 2:
                ejecutar_operacion_basica(restar, "resta")
            
            elif opcion == 3:
                ejecutar_operacion_basica(multiplicar, "multiplicación")
            
            elif opcion == 4:
                ejecutar_operacion_basica(dividir, "división")
            
            elif opcion == 5:
                print("\n--- SUMA AVANZADA ---")
                numeros = obtener_varios_numeros()
                
                if len(numeros) == 0:
                    print("No se ingresaron números.")
                else:
                    resultado = sumar_varios(*numeros)
                    numeros_str = " + ".join(map(str, numeros))
                    print(f"Resultado: {numeros_str} = {resultado}")
            
            elif opcion == 6:
                print("¡Gracias por usar la Calculadora Modular!")
                break
            
            else:
                print("Opción inválida. Por favor seleccione una opción del 1 al 6.")
        
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Gracias por usar la Calculadora Modular!")
            break


if __name__ == "__main__":
    main()