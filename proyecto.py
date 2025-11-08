"""
Práctica Unidades 1 y 2 — PROYECTOS II

Instrucciones generales:
- Este archivo se completará por etapas en distintas ramas de Git.
- NO cambies los nombres de las funciones ni sus parámetros.
- Puedes añadir funciones auxiliares si lo necesitas.
- Al finalizar, todas las funciones deben estar implementadas y probadas (puedes ejecutar tests propios).
"""

# === IMPORTS (añade otros si son necesarios) ===
import csv, json, os, random, math
from datetime import datetime
from typing import List, Dict, Optional

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, integrate, interpolate

# 1) Básicos y cadenas
def sum_even(nums: List[int]) -> int:
    evenList: list[int] = []
    finalResult: int = 0

    for i in nums:
        if i % 2 == 0:
            evenList.append(i)

    for even in evenList:
        finalResult += even

    print(f"La suma total de los números pares es: ", finalResult)

    return int(bool(finalResult != 0)) #Devolvemos 0 o 1, si finalResult es distinto de 0 (hay pares), con bool, lo volvemos true o false y traducimos eso con int a 1 o 0
    """Suma los enteros pares de la lista. Si no hay pares, devuelve 0."""


def normalize_str(s: str) -> str:
    """Devuelve s sin espacios al inicio/fin y en minúsculas."""
    wordRefactored: str = s.strip()
    return wordRefactored.lower()


def count_words(text: str) -> Dict[str, int]:
    """
      Devuelve un dict palabra->frecuencia.
      Reglas: separa por espacios; elimina . , ; : ! ? al final de cada token; ignora mayúsculas.
      """

    myDictionary: dict[str, int] = {}
    notPermittedSigns: list[str] = [".", ",", ";", ":", "!", "?"]
    wordsSplited: list[str] = text.split()

    for i in range(len(wordsSplited)):
        wordsSplited[i] = wordsSplited[i].strip("".join(notPermittedSigns)).lower() #Unimos a una cadena vacia los signos no permitidos y eliminamos el correspondiente de la palabra indicada
        counter: int = 0
        for j in wordsSplited:
            if wordsSplited[i] == j: #Pivotamos sobre cada j (palabra) y comparamos con el array de wordsSplited
                counter += 1
            myDictionary[wordsSplited[i]] = counter #Creamos dinamicamente el diccionario con su clave - frecuencia correspondiente

    print("Diccionario final", myDictionary)
    return myDictionary


# 2) Ficheros y excepciones
def safe_divide(a: float, b: float) -> Optional[float]:
    """Devuelve a/b. Si b==0 o hay error, devuelve None."""
    pass


def read_csv_sum_revenue(path: str) -> float:
    """
    Lee un CSV con columnas units_sold y unit_price.
    Convierte a numérico; ignora NaN o negativos; suma units_sold*unit_price.
    """
    pass


def filter_customers_json(in_path: str, out_path: str) -> int:
    """
    JSON (lista de objetos con email y age).
    Escribe en out_path solo clientes con email que contenga '@' y age > 0.
    Devuelve el número de clientes escritos.
    """
    pass


# 3) Comprensiones, random, datetime
def squares_of_odds(n: int) -> List[int]:
    """Lista de cuadrados de impares 1..n (ambos inclusive)."""
    pass


def random_color(seed: int) -> str:
    """Fija random.seed(seed) y retorna un color aleatorio de ['rojo','azul','verde']."""
    pass


def days_between(d1: str, d2: str) -> int:
    """Recibe fechas 'YYYY-MM-DD'. Devuelve abs(d2-d1) en días (entero)."""
    pass


# 4) NumPy
def numpy_vector_length(v: List[float]) -> float:
    """Norma Euclídea de v con NumPy."""
    pass


def numpy_minmax_scale(arr: List[float]) -> List[float]:
    """
    Normaliza a [0,1]. Si todos los valores son iguales, devuelve todos 0.0.
    """
    pass


# 5) SciPy
def scipy_root_cos_minus_x() -> float:
    """Raíz de f(x)=cos(x)-x con optimize.root, x0=0.5."""
    pass


def scipy_integral_sin() -> float:
    """Integral de sin(x) de 0 a pi con integrate.quad. Devuelve el área."""
    pass


def interp_linear(x: List[float], y: List[float], xq: float) -> float:
    """Interpolación lineal: devuelve f(xq) usando interpolate.interp1d."""
    pass


# 6) Visualización
def plot_line_time_series(xs: List[float], ys: List[float], out_path: str) -> bool:
    """
    Dibuja línea con título y etiquetas. Guarda en out_path y devuelve True si existe.
    """
    pass


def plot_bar(categories: List[str], values: List[float], out_path: str) -> bool:
    """Barras con etiquetas. Guarda y devuelve True si existe."""
    pass


def plot_scatter(x: List[float], y: List[float], out_path: str) -> bool:
    """Dispersión con grid y legend (usa label). Guarda y devuelve True si existe."""
    pass


# 7) POO
class Vector2D:
    """
    Implementa:
      - __init__(x, y)
      - __add__(other): suma vectorial, devuelve Vector2D
      - __eq__(other): igualdad por componentes
      - __repr__(): 'Vector2D(x=?, y=?)'
      - length(self) -> float: norma Euclídea
    """
    pass
