"""
func_numericas.py
Funciones numéricas reutilizables para el backend.
"""
from typing import Iterable, List, Union
import math
import numpy as np

Number = Union[int, float]


def MCD(value_1: int, value_2: int) -> int:
    """Calcula el máximo común divisor (MCD) entre dos enteros."""
    if not isinstance(value_1, int) or not isinstance(value_2, int):
        raise ValueError("Ambos valores deben ser enteros.")
    if value_1 < 0 or value_2 < 0:
        return 1
    return math.gcd(value_1, value_2)


def iterable_MCD(lista_num: Iterable[int]) -> int:
    """Calcula el MCD de una colección de enteros aplicando MCD de a pares."""
    if not isinstance(lista_num, (list, tuple)):
        raise ValueError("Se debe enviar una lista o tupla de enteros.")
    lista = list(lista_num)
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")
    for i, el in enumerate(lista):
        if not isinstance(el, int):
            raise ValueError(f"Elemento en posición {i} no es entero: {el}")
    current = lista[0]
    for n in lista[1:]:
        current = MCD(current, n)
    return current


def media(lista_num: Iterable[Number]) -> float:
    """Calcula la media aritmética de una colección de números."""
    if not isinstance(lista_num, (list, tuple)):
        raise ValueError("Se debe enviar una lista o tupla de números.")
    arr = np.array(lista_num)
    if not np.issubdtype(arr.dtype, np.number):
        raise ValueError("Todos los elementos deben ser numéricos.")
    return float(round(float(np.mean(arr)), 3))


def sigma(lista_num: Iterable[Number]) -> float:
    """Calcula la desviación estándar de la colección."""
    if not isinstance(lista_num, (list, tuple)):
        raise ValueError("Se debe enviar una lista o tupla de números.")
    arr = np.array(lista_num)
    if not np.issubdtype(arr.dtype, np.number):
        raise ValueError("Todos los elementos deben ser numéricos.")
    return float(round(float(np.std(arr)), 3))


def num_primo(num: int) -> bool:
    """Verifica si un número entero positivo es primo."""
    if not isinstance(num, int):
        return False
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def primalidad_lista(lista_num: Iterable[int]) -> List[int]:
    """Filtra y retorna sólo los números primos de la lista."""
    if not isinstance(lista_num, (list, tuple)):
        raise ValueError("Se debe enviar una lista o tupla de números.")
    primes = []
    for el in lista_num:
        if isinstance(el, (int, float)) and float(el).is_integer():
            val = int(el)
            if val > 1 and num_primo(val):
                primes.append(val)
    return primes


if __name__ == "__main__":
    pass
