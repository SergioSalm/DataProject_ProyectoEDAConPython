import pandas as pd
import numpy as np

def calcular_nulos(df):
    """Función para calcular número de nulos y porcentaje de nulos por columna.

    Args:
        df (df.pandas): dataFrame a analizar
    Returns:
        tupla: dos series de pandas con el número de nulos y el porcentaje de nulos
    """
    numero_nulos = df.isnull().sum()
    pct_nulos = (df.isnull().sum() / df.shape[0]) * 100

    return numero_nulos, pct_nulos

def analisis_general_categoricas(df):
    """Función que muesta por pantalla el análisis de las columnas categóricas

    Args:
        df (df.pandas): dataFrame a analizar
    """
    col_categoricas = df.select_dtypes(include='O').columns

    if len(col_categoricas) == 0:
        print ("No hay columnas categoricas")
    else:
        for col in col_categoricas:
            print(f"Distribución de la columna {col.upper()}")
            print(f"    {len(df[col].unique())} valores únicos")
            display(df[col].value_counts(normalize=True)) # type: ignore
            print(f"    Describe")
            display(df[col].describe()) # type: ignore
            print("----------------")