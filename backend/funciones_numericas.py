# backend/funciones_numericas.py
# https://github.com/Mariagustin-Prg/analizador-series-numericas
''' 
Funciones numéricas para el análisis de series numéricas. 
''' 

import numpy as np
from typing import Iterable

def MaximoComunDivisor(value_1: int, value_2: int) -> int:
    """
    Calcula el máximo común divisor (MCD) de dos números enteros.

    Args:
        value_1 (int): Primer número entero.
        value_2 (int): Segundo número entero.

    Returns:
        int: El máximo común divisor de los dos números.
    """
    if not (isinstance(value_1, int) and not isinstance(value_2, int)): # Si no se ingresan dos enteros
        raise ValueError("Ambos valores deben ser enteros.") # Retorna un error
    
    min_value = min(value_1, value_2)

    for i in range(min_value, 0, -1): # Recorre desde el valor mínimo de entre los dos valores hasta 1
        if value_1 % i == 0 and value_2 % i == 0: # Verifica que ambos valores sean divisibles por i
            return i # Si ambos valores son divisibles por i, entonces i es el MCD
        
def MCD_iterable(values: Iterable[int]) -> int:
    """
    Calcula el máximo común divisor (MCD) de una lista de números enteros.

    Args:
        values (Iterable[int]): Una lista o iterable de números enteros.

    Returns:
        int: El máximo común divisor de los números en la lista.
    """
    
    mcd = values[0] # Inicializa el MCD con el primer valor de la lista

    for value in values[1:]: # Recorre los valores restantes en la lista
        mcd = MaximoComunDivisor(mcd, value) # Actualiza el MCD con el MCD del valor actual y el MCD anterior

    return mcd # Retorna el MCD final


# --------------------------------------------------
# Media y Desviación Estándar
def media(values: Iterable[int]) -> float:
    """
    Calcula la media (promedio) de una lista de números.

    Args:
        values (Iterable[int]): Una lista o iterable de números.

    Returns:
        float: La media de los números en la lista.
    """
    return np.mean(values) # Retorna la media de los valores usando numpy

def sigma(values: Iterable[int]) -> float:
    """
    Calcula la desviación estándar de una lista de números.

    Args:
        values (Iterable[int]): Una lista o iterable de números.

    Returns:
        float: La desviación estándar de los números en la lista.
    """
    return np.std(values) # Retorna la desviación estándar de los valores usando numpy

# --------------------------------------------------
# Primalidad de números
def es_primo(n: int) -> bool:
    """
    Determina si un número es primo.

    Args:
        n (int): El número a verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if n <= 1: # Si n es menor o igual a 1, no es primo
        return False # Retorna Falso
    
    for i in range(2, int(np.sqrt(n)) + 1, 1):  # Recorre desde 2 hasta la raíz cuadrada de n
        if n % i == 0: # Si n es divisible por i, entonces no es primo
            return False # Retorna Falso
        
    return True # Si no se encontró ningún divisor, entonces n es primo, retorna True

def primos_en_lista(values: Iterable[int]) -> list[int]:
    """
    Filtra y retorna los números primos de una lista.

    Args:
        values (Iterable[int]): Una lista o iterable de números enteros.

    Returns:
        list[int]: Una lista de números primos encontrados en la entrada.
    """
    primos = [value for value in values if es_primo(value)] # Usa una comprensión de listas para filtrar los números primos
    return primos # Retorna la lista de números primos