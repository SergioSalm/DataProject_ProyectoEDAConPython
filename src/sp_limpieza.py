import pandas as pd
import numpy as np

def eda_preliminar (df):
    """Función que analiza el df e imprime los resultados por pantalla

    Args:
        df (df.pandas): dataFrame a analizar
    """
    display(df.sample(5))   # type: ignore

    display(df.describe().T) # type: ignore

    print('------------------------')

    print ('INFO')

    display(df.info())  # type: ignore

    print('------------------------')

    print ('NULOS')    

    display(round(df.isnull().sum()/df.shape[0]*100, 2))     # type: ignore

    print('------------------------')

    print ('DUPLICADOS')    

    display(df.duplicated().sum())    # type: ignore

    print('------------------------')

    display(df.describe(include='O').T) # type: ignore

    print ('VALUE COUNTS')    

    for col in df.select_dtypes(include ='O').columns:
        print(df[col].value_counts())
        print('------------------')    

def valores_minus (df):
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.lower()

def comas(df, lista_col):
    """Función que cambia las comas por las puntos en las columnas del df indicadas

    Args:
        df (df.pandas): dataFrame a cambiar
        lista_col (lista): Lista de columnas del df a canbiar
    """
    for col in lista_col:
            df[col] = df[col].str.replace(',','.')

def convertir_enteros(df):
    """Función que convierte la columna a float o a int

    Args:
        df (df.pandas): dataFrame a cambiar
    """
    for col in df.columns:
        if df[col].dtype == 'O':
            for dtype in [float, int]:   
                try:
                    df[col] = df[col].astype(dtype)
                except:
                     pass       
        
def convertir_fechas(df, fecha_formato):
    """Función que convierte una columna al formato DateTime. 

    Args:
        df (df.pandas): dataFrame a cambiar
        fecha_formato (Diccionario): Diccionario que contiene las columnas junto con el formarto a aplicar en cada columna.
    """
    for col, formato in fecha_formato.items():
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format=formato)
            
def convertir_YesNo(df, lista_col):
    """Función que convierte los valores 1,0,nan a 'Yes', 'No' y 'None' en las columnas del df indicadas

    Args:
        df (df.pandas): dataFrame a cambiar
        lista_col (lista): Lista de columnas del df a canbiar
    """
    for col in lista_col:
        df[col] = df[col].map({1:"yes", 0:"no", np.nan: 'None'})

def clasificar_valores(df, columna_origen, columna_nueva, bins, valores):
    df[columna_nueva] = pd.cut(df[columna_origen],
                                bins=bins,
                                labels=valores
                           )