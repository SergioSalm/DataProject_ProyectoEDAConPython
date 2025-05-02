import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def subplot_col_cat(df, columnas):
    """Función que muestra por pantalla los subplots de las columnas categóricas

    Args:
        df (df.pandas): dataFrame a analizar
        columnas (List): columnas a tener en cuenta en los gráficos
    """
   
    if (len(columnas)) == 0:
        print("No hay columnas categóricas")
        return
    
    #Configurar el tamaño de la figura
    num_cols = len(columnas)
    num_rows = (num_cols + 2) // 3 #Calcular filas necesarias para 3 columnas por fila
    fig, axes = plt.subplots(num_rows, 3, figsize=(15, num_rows * 5))
    axes = axes.flatten() #Convertir los ejes a un arreglo plano para fácil iteración.

    #Generar gráfico para cada columna categórica
    for i, col in enumerate(columnas):
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


def subplot_col_num(df, columnas):
    """Función que muestra por pantalla los subplots de las columnas numéricas

    Args:
        df (df.pandas): dataFrame a analizar
        columnas (List): columnas a tener en cuenta en los gráficos
    """
    
    if (len(columnas)) == 0:
        print("No hay columnas numéricas")
        return
    
    #Configurar el tamaño de la figura
    num_cols = len(columnas)
    num_rows = (num_cols + 2) // 2 #Calcular filas necesarias para 3 columnas por fila
    fig, axes = plt.subplots(num_cols, 2, figsize=(15, num_rows * 5))
    #axes = axes.flatten() #Convertir los ejes a un arreglo plano para fácil iteración.

    for i, col in enumerate(columnas):
        #histogramas
        sns.histplot(data=df, x=col, ax=axes[i, 0], bins=200)
        axes[i, 0].set_title(f'Distribución de {col}')
        axes[i, 0].text(0.8, 0.9, f'Media: {round(df[col].mean(), 4)}', horizontalalignment='center', verticalalignment='center', transform=axes[i, 0].transAxes)
        axes[i, 0].text(0.8, 0.8, f'Mediana: {round(df[col].median(), 4)}', horizontalalignment='center', verticalalignment='center', transform=axes[i, 0].transAxes)
        axes[i, 0].set_ylabel('Frecuencia')

        #boxplots
        min = int(df[col].min())
        max = int(df[col].max())

        sns.boxplot(data=df, x=col, ax=axes[i, 1],)
        axes[i, 1].set_title(f'Boxplot de {col}')
        #axes[i, 1].set_xticks(ticks=np.arange(min, max + 1, 2))  

    #Eliminar ejes sobrantes si hay menos columnas que subplots. Eliminamos gráficas vacías.
    for j in range(i +1, len(axes)):
        fig.delaxes(axes[j])


    #ajustar diseño
    plt.tight_layout()
    plt.show()