import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, KNNImputer

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


def visualizar_nulos_categoricas(df, umbral_pct_null = 10, umbral_pct_value = 80):
    null_columns = df.columns[df.isnull().any()]        

    if len(null_columns) == 0:
        print ("No hay nulos")

    null_columns_info = pd.DataFrame(
        {"Columns": null_columns,
         "DataType": [df[col].dtype for col in null_columns],
         "Num_nulls": [df[col].isnull().sum() for col in null_columns],
         "%_null": [((df[col].isnull().sum() / df.shape[0]) * 100) for col in null_columns],
         "Change_value": [(((df[col].isnull().sum() / df.shape[0]) * 100) < umbral_pct_null and ((df[col].value_counts(normalize=True).max() * 100) > umbral_pct_value)) for col in null_columns],
         "Change_By": [((df[col].value_counts(normalize=True)).idxmax()) for col in null_columns],
         "%": [((df[col].value_counts(normalize=True)).max()) for col in null_columns] 
        }
    )   

    display (null_columns_info)# type: ignore

    col_high_umbral = null_columns_info[null_columns_info['%_null'] > umbral_pct_null]['Columns'].tolist()
    col_low_umbral = null_columns_info[null_columns_info['%_null'] <= umbral_pct_null]['Columns'].tolist()

    return col_high_umbral, col_low_umbral

def visualizar_nulos_numericos(df, umbral_pct_null = 10):
    null_columns = df.columns[df.isnull().any()]        

    if len(null_columns) == 0:
        print ("No hay nulos")

    null_columns_info = pd.DataFrame(
        {"Columns": null_columns,
        "DataType": [df[col].dtype for col in null_columns],
        "Num_nulls": [df[col].isnull().sum() for col in null_columns],
        "%_null": [((df[col].isnull().sum() / df.shape[0]) * 100) for col in null_columns],
        "Change_value": [(((df[col].isnull().sum() / df.shape[0]) * 100) < umbral_pct_null ) for col in null_columns],
        "Media": [df[col].mean() for col in null_columns],
        "Mediana": [df[col].median() for col in null_columns] 
        }
    )   

    display (null_columns_info)# type: ignore

    col_high_umbral = null_columns_info[null_columns_info['%_null'] > umbral_pct_null]['Columns'].tolist()
    col_low_umbral = null_columns_info[null_columns_info['%_null'] <= umbral_pct_null]['Columns'].tolist()
    return col_high_umbral, col_low_umbral
    

def imputar_iterative(df, lista_columnas):
    iter_imputer = IterativeImputer(max_iter=50, random_state=42)
    data_imputed = iter_imputer.fit_transform(df[lista_columnas])
    new_col = [col + "_iterative" for col in lista_columnas]

    df[new_col] = data_imputed
    display (df[new_col].describe().T)# type: ignore
    return df, new_col

def imputar_knn(df, lista_columnas):
    knn_imputer = KNNImputer(n_neighbors=5)
    data_imputed = knn_imputer.fit_transform(df[lista_columnas])
    new_col = [col + "_knn" for col in lista_columnas]

    df[new_col] = data_imputed
    display (df[new_col].describe().T)# type: ignore
    return df, new_col
