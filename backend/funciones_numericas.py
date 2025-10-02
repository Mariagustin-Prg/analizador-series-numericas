# backend/funciones_numericas.py
''' 
Funciones numéricas para el análisis de series numéricas. 
''' 


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