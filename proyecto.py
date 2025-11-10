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
import pandas as pd
import random as rand
from datetime import datetime
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy import optimize, integrate, interpolate

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
    try :
        division : float =  a / b
        print("División final: ", division)
    except Exception as e:
        print("Ha habido un error: ",e)
    finally:
        print("Fin del programa")
        return None


def read_csv_sum_revenue(path: str) -> float: #REVISAR
    """
    Lee un CSV con columnas units_sold y unit_price.
    Convierte a numérico; ignora NaN o negativos; suma units_sold*unit_price.
    """
    unitsCSV = pd.read_csv(path)
    for row in unitsCSV.itertuples(index=False):
        units = row.units_sold
        prize = row.unit_price
        finalResult = units*prize
        print(f"Unidades:{units}, Precio/u:{prize}, Resultado:{finalResult}")
    pass


def filter_customers_json(in_path: str, out_path: str) -> int:
    """
    JSON (lista de objetos con email y age).
    Escribe en out_path solo clientes con email que contenga '@' y age > 0.
    Devuelve el número de clientes escritos.
    """
    usersJSON = pd.read_json(in_path)
    usersFiltered : list = []
    for users in usersJSON.itertuples(index=False): #Lo convertirmos a tuplas
        userEmail = users.email
        userAge = users.age
        if "@" in userEmail and userAge > 0: #filtramos
            usersFiltered.append({"email":userEmail,"age":userAge})

    pd.DataFrame(usersFiltered).to_json(out_path, orient="records", indent=2) #Convertimos la lista en un dataFrame, y con to_json, escribimos en out_path, dándole orientación de tipo "records" y una indentación para que se vea mas bonito
    print("Nuevo JSON: ", usersFiltered)
    print("Usuarios anadidos:", len(usersFiltered))
    return len(usersFiltered)


# 3) Comprensiones, random, datetime
def squares_of_odds(n: int) -> List[int]:
    """Lista de cuadrados de impares 1..n (ambos inclusive)."""
    impares = [i**2 for i in range(1,n + 1) if i % 2 != 0]
    print(impares)
    return impares


def random_color(seed: int) -> str:
    """Fija random.seed(seed) y retorna un color aleatorio de ['rojo','azul','verde']."""
    rand.seed(seed)
    print(random.choice(['rojo','azul','verde']))
    return random.choice(['rojo','azul','verde'])


def days_between(d1: str, d2: str) -> int:
    """Recibe fechas 'YYYY-MM-DD'. Devuelve abs(d2-d1) en días (entero)."""
    print("Diferencia de dias:",abs((datetime.strptime(d2, '%Y-%m-%d' ))-(datetime.strptime(d1, '%Y-%m-%d' ))))
    return abs((datetime.strptime(d2, '%Y-%m-%d' ))-(datetime.strptime(d1, '%Y-%m-%d' )))


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

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self,other):
        return self.x == other.x and self.x == other.y

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    pass
