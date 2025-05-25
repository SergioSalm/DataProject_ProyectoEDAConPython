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

def barplot_compareCat(df, col1, col2, columnas):
    """Genera una serie de subgráficos comparativos para variables categóricas.

    Para cada columna categórica en `columnas`, se generan 3 gráficos:
    1. Conteo de categorías.
    2. Porcentaje de valores 'yes' en `col1`.
    3. Porcentaje de valores 1 en `col2`.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        col1 (str): Nombre de columna con valores tipo 'yes'/'no'.
        col2 (str): Nombre de columna binaria con 1/0 (ej. éxito en primer contacto).
        columnas (list): Lista de nombres de columnas categóricas a analizar.

    Returns:
        None
    """
    num_cols = len(columnas)
    num_rows = (num_cols + 2) // 3 #Calcular filas necesarias para 3 columnas por fila
    fig, axes = plt.subplots(num_cols, 3, figsize=(15, num_rows * 10))


    for i, col in enumerate(columnas):
        categorias_ordenadas = sorted(df[col].unique())

        countplot = sns.countplot(data = df, x=col, hue=col, ax=axes[i,0], legend=False, order=categorias_ordenadas, palette="tab10")
        axes[i, 0].set_title(f'Clientes contactados a través de {col}')
        axes[i, 0].set_ylabel('Total')
        axes[i, 0].tick_params(axis='x', rotation=90) 

        for p in countplot.patches:
            height = p.get_height()
            countplot.text(
                x=p.get_x() + p.get_width() / 2,
                y=height,
                s=f"{height:.2f}",
                ha='center',
                va='bottom',
                fontsize=10,
                fontweight='bold'
            )

        df1 = df.groupby(col)[col1].apply(lambda x: (x=='yes').mean()).reset_index()
        barplot = sns.barplot(data = df1, x=col, y =df1[col1], hue=col, ax=axes[i,1], legend=False, order=categorias_ordenadas, palette="tab10") 
        axes[i, 1].set_title(f'Clientes suscritos a través de {col}')
        axes[i, 1].set_ylabel('Porcentaje')
        axes[i, 1].tick_params(axis='x', rotation=90) 
        
        for p in barplot.patches:
            height = p.get_height()
            barplot.text(
                x=p.get_x() + p.get_width() / 2,
                y=height,
                s=f"{height:.2f}",
                ha='center',
                va='bottom',
                fontsize=10,
                fontweight='bold'
            )

        df2 = df.groupby(col)[col2].apply(lambda x: (x==1).mean()).reset_index()
        barplot = sns.barplot(data = df2, x=col, y =df2[col2], hue=col, ax=axes[i,2], legend=False, order= categorias_ordenadas, palette="tab10")
        axes[i, 2].set_title(f'Clientes suscritos al primer contacto a través de {col}')
        axes[i, 2].set_ylabel('Porcentaje')
        axes[i, 2].tick_params(axis='x', rotation=90) 
        for p in barplot.patches:
            height = p.get_height()
            barplot.text(
                x=p.get_x() + p.get_width() / 2,
                y=height,
                s=f"{height:.2f}",
                ha='center',
                va='bottom',
                fontsize=10,
                fontweight='bold'
            )

        
    plt.tight_layout()
    plt.show()

def barplot_compareCol(df, col1, col2):
    """
    Crea un gráfico de barras que muestra la proporción de valores de `col2` agrupados por `col1`.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        col1 (str): Columna categórica base para agrupar.
        col2 (str): Columna categórica cuya distribución proporcional se quiere visualizar.

    Returns:
        None
    """
    prop_df = (
        df.groupby(col1)[col2]
        .value_counts(normalize=True)
        .rename('proportion')
        .reset_index()
    )
  
    figsize=(8, 6)
    plt.figure(figsize=figsize)
    sns.barplot(data=prop_df, x=col1, y='proportion', hue=col2)
    plt.title(f"Proporción de '{col2}' por '{col1}'")
    plt.ylabel("Proporción")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()