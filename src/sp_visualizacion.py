import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def subplot_col_cat(df):
    """Función que muestra por pantalla los subplots de las categóricas

    Args:
        df (df.pandas): dataFrame a analizar
    """
    #seleccionamos columnas categóricas
    col_cat = df.select_dtypes(include=['object', 'category']).columns
    
    if (len(col_cat)) == 0:
        print("No hay columnas categóricas")
        return
    
    #Configurar el tamaño de la ficgura
    num_cols = len(col_cat)
    rows = (num_cols + 2) // 3 #Calcular filas necesarias para 3 columnas por fila
    fig, axes = plt.subplots(rows, 3, figsize=(15, rows * 5))
    axes = axes.flatten() #Convertir los ejes a un arreglo plano para fácil iteración.

    #Generar gráfico para cada columna categórica
    for i, col in enumerate(col_cat):
        sns.countplot(data=df, x=col, ax=axes[i], hue=col, palette="tab10", legend=False)
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')
        axes[i].tick_params(axis='x', rotation=90) #Rotar etiquetas si es necesario

    #Eliminar ejes sobrantes si hay menos columnas que subplots. Eliminamos gráficas vacías.
    for j in range(i +1, len(axes)):
        fig.delaxes(axes[j])

    #ajustar diseño
    plt.tight_layout()
    plt.show()