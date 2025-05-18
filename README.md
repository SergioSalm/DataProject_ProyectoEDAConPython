# 🌟 Análisis de Campaña de Marketing Bancario en Portugal

![Portada del Proyecto](https://images.unsplash.com/photo-1581090700227-1e8e1a236a59?auto=format\&fit=crop\&w=1350\&q=80)

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-blueviolet)](https://seaborn.pydata.org/)

---

## 🔍 Descripción del Proyecto

Este proyecto tiene como objetivo analizar los datos de una campaña de marketing de un banco portugués orientada a la contratación de depósitos a plazo. A través del análisis de datos demográficos y conductuales de los clientes, se busca identificar patrones comunes entre los clientes que se han suscrito al producto, y proponer estrategias de mejora en la segmentación y eficiencia de futuras campañas.

---

## 📂 Tabla de Contenidos

* [Datos Utilizados](#datos-utilizados)
* [Proceso de Análisis](#proceso-de-análisis)

  * [Limpieza de Datos](#limpieza-de-datos)
  * [Análisis Exploratorio](#análisis-exploratorio)
  * [Visualización](#visualización)
* [Principales Hallazgos](#principales-hallazgos)
* [Visualizaciones](#visualizaciones)
* [Conclusiones y Recomendaciones](#conclusiones-y-recomendaciones)
* [Instalación y Configuración](#instalación-y-configuración)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Guía de Uso](#guía-de-uso)
* [Próximos Pasos](#próximos-pasos)
* [Contribución y Contacto](#contribución-y-contacto)
* [Licencia](#licencia)
* [Agradecimientos](#agradecimientos)

---

## 📅 Datos Utilizados

* **Fuente:** [thePower- DataProject: Proyecto EDA con Python](https://s3.amazonaws.com/staticcontent.thepowermba/Bootcamp+Data+%26+Analytics/D%26A24/Phyton/DatosProyecto.rar)

* **Fichero bank-additional.csv** 
    * **Filas:** 43.000  
    * **Columnas:** 23
    * **Observaciones:** Tenemos 10 columnas con valores nulos. El tipo de datos de los valores de algunas columnas es incorrecto

    ### Diccionario de Datos Resumido

    | Columna    | Descripción                       | Tipo       |
    | ---------- | --------------------------------- | ---------- |
    | age        | Edad del cliente                  | Numérico   |
    | job        | La ocupación o profesión del cliente   | Categórico |
    | marital    | Estado civil                      | Categórico |
    | education  | Nivel educativo                   | Categórico |
    | default    | Indica si el cliente tiene algún historial de incumplimiento de pagos (1: Sí, 0: No)            | Binario    |
    | housing    | ¿Tiene préstamo de vivienda? (1: Sí, 0: No)      | Binario    |
    | loan       | ¿Tiene otro préstamo personal? (1: Sí, 0: No)    | Binario    |
    | contact    | Método de contacto utilizado para comunicarse con el cliente                  | Categórico |    
    | duration   | Duración de última llamada (seg)  | Numérico   |
    | campaign   | Nro. de contactos durante campaña | Numérico   |
    | pdays      | Número de días que han pasado desde la última vez que se contactó con el cliente durante esta campaña     | Numérico    |
    | previous   | Número de veces que se ha contactado con el cliente antes de esta campaña                 | Numérico   |
    | poutcome   | Resultado de la campaña de marketing anterior                         | Categórico |
    | emp.var.rate    | La tasa de variación del empleo                      | Numérico |
    | cons.price.idx  | El índice de precios al consumidor                  | Categórico |
    | cons.conf.idx    | El índice de confianza del consumidor           | Categórico    |
    | euribor3m    | La tasa de interés de referencia a tres meses      | Categórico    |
    | nr.employed       | El número de empleados   | Categórico    |
    | y    | Indica si el cliente ha suscrito un producto o servicio (Sí/No)                  | Categórico |    
    | date   | La fecha en la que se realizó la interacción con el cliente   |
    | latitude   | Columna erronea | Numérico   |
    | longitude      | Columna erronea     | Numérico    |
    | id_      | Un identificador único para cada registro en el dataset.     | Categórico    |

* **Fichero customer-detail.xlxs**
    * **Observaciones:** Este fichero consta de 3 hojas. Las 3 hojas tienen las mismas columnas con el mismo nombre. Agrupamos las 3 hojas en un solo dataframe. Las columnas no tienen valores nulos.

     ### Diccionario de Datos Resumido

    | Columna    | Descripción                       | Tipo       |
    | ---------- | --------------------------------- | ---------- |
    | Income        | Representa el ingreso anual del cliente en términos monetarios                 | Numérico   |
    | Kidhome       | Indica el número de niños en el hogar del cliente                         | Numérico |
    | Teenhome      | Indica el número de adolescentes en el hogar del cliente                     | Numérico |
    | Dt_Customer   | Representa la fecha en que el cliente se convirtió en cliente de la empresa                  | Fecha / hora |
    | NumWebVisitsMonth    | Indica la cantidad de visitas mensuales del cliente al sitio web de la empresa           | Numérico    |
    | ID    | Identificador único del cliente     | Categórico    |
    


## ⚖️ Proceso de Análisis

### 🚼 Limpieza de Datos
* Eliminamos las columnas 'latitude' y 'longitude'.
* Convertimos todos los datos del dataframe a minúsculas para homogeneizar los datos.  
* Sustituimos las "," por los puntos en las columnas 'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed'.  
* Hacemos una conversión en la columna date, donde cambiamos el nombre del mes por el número correspondiente.  
* Cambiamos el tipo de datos de las columnas de tipo fecha y de las columnas de tipo numéricas.
* Cambiamos los valores 1, 0, nan por 'Yes', 'No', 'None' en las columnas 'default', 'housing' y 'loan'
* En la columna 'pdays', cambiamos el valor 999 por -1, para tener los datos más agrupados.

* Creamos las nuevas columnas:
    * contact_year: año de la interacción del banco con el cliente
    * contact_month: mes de la interacción del banco con el cliente
    * customer_year: año en el que se convirtió en cliente de la empresa.
    * customer_month: mes en el que se convirtió en cliente de la empresa.
    * Creamos la columna 'subscribed' para tener un título más aclarativo y borramos la columna original 'y'.  
    * Creamos la columna 'duration_min' para tener los tiempos de las llamadas en minutos y eliminamos la columna 'duration'. 

### 💡 Análisis Exploratorio
PENDIENTE
* Distribuciones univariadas y bivariadas.
* Segmentación por estado civil, profesión, edad, y contacto.
* Cálculo de tasas de conversión por grupo.

### 🎨 Visualización

* Gráficos de barra (countplot), histogramas (histplot), diagramas de caja (boxplot) y diagramas de barra (barplot) para detectar patrones.

---

## 📊 Principales Hallazgos

* **Tasa de conversión general:** `tasa = 11,27%`
* **Tasa de resolución en el primer contacto:** `tasa = 5,57%`
* Clientes **mayores de 50** y aquellos con **contacto mediante "cellular"** tienen mayor conversión.
* Profesiones como "student" y "retired" muestran tasas altas de suscripción.
* La variable `duration` (duración de llamada) tiene alta correlación con el resultado.

---

## 🖼️ Visualizaciones

* ![placeholder1](https://via.placeholder.com/600x300.png?text=Gr%C3%A1fico+1:+Tasa+de+Conversi%C3%B3n+por+Edad)

  > **Gráfico 1:** Relación entre edad y tasa de suscripción.
* ![placeholder2](https://via.placeholder.com/600x300.png?text=Gr%C3%A1fico+2:+Profesiones+con+mejor+rendimiento)

  > **Gráfico 2:** Profesiones con mayor % de conversión.
* ![placeholder3](https://via.placeholder.com/600x300.png?text=Gr%C3%A1fico+3:+Contactabilidad+y+conversiones)

  > **Gráfico 3:** Impacto del tipo de contacto.

---

## 📖 Conclusiones y Recomendaciones

* **Segmentar futuras campañas** hacia personas mayores, jubilados o estudiantes.
* Priorizar el uso de **contacto telefónico celular**.
* Invertir en llamadas de mayor duración (indicador indirecto de interés).
* Excluir perfiles con baja probabilidad para mejorar ROI.

---

## 🛠️ Instalación y Configuración en windows

```bash
# Clona el repositorio
git clone https://github.com/SergioSalm/DataProject_ProyectoEDAConPython.git
cd nombre_del_repositorio

# Crea un entorno virtual (opcional)
python3 -m venv venv
source venv/Scripts/activate

# Instala dependencias
pip install -r requirements.txt
```

---

## 📁 Estructura del Proyecto

```
.
├── data/                 # Datos brutos o preprocesados
│  ├─ Orig                    #Carpeta con los archivos originales
│  │  ├─ bank-additional.csv
│  │  ├─ customer-details.xlsx
│  ├─ transformados                    #Carpeta con los archivos originales
│  │  ├─ bank-customers-detail.csv
│  ├─ data-clean.csv                    #Carpeta con los archivos originales
│  ├─ data-metricas.csv                    #Carpeta con los archivos originales
├── jupyters/             # Jupyter Notebooks con el análisis
│  ├─ Orig   
│  ├─ Orig   
│  ├─ Orig   
│  ├─ Orig   
│  ├─ Orig   
├── images/               # Visualizaciones exportadas
├── src/                  # Scripts auxiliares
│  ├─ Orig   
│  ├─ Orig   
│  ├─ Orig   
├── README.md             # Documentación principal
└── requirements.txt      # Dependencias del proyecto
```

---

## 🔧 Guía de Uso

1. Abre la carpeta jupyters y ejecuta los ficheros en el siguiente orden:
    - [1-EDA_preliminar.ipynb](jupyters/1-EDA_preliminar.ipynb)
    - [2-limpieza.ipynb](jupyters/2-limpieza.ipynb)
    - [3-columnas_categoricas.ipynb](jupyters/3-columnas_categoricas.ipynb)
    - [4-columnas_numericas.ipynb](jupyters/4-columnas_numericas.ipynb)
    - [5-marketing.ipynb](jupyters/5-marketing.ipynb)

2. Ejecuta célula por célula para replicar el análisis.
3. Revisa los gráficos generados y modifica filtros para nuevas segmentaciones.

---

## 📈 Próximos Pasos

* Implementar modelos predictivos.
* Automatizar el análisis para nuevas campañas.

---

## 🛠️ Contribución y Contacto

¡Contribuciones bienvenidas! Abre un pull request o contacta:

* Sergio Salmerón - [GitHub Profile](https://github.com/SergioSalm)

---

## ✉️ Licencia



---

## 🙏 Agradecimientos

Gracias a:

* **thePower Business School** por ofrecer el curso y la guía en el desarrollo de este proyecto de análisis de datos.
* Comunidad de Python y Data Science por recursos y documentación.

---


--------------------------------------------------------------------

## Herramientas utilizadas
Python (Pandas, seaborn, matplotlib)
Jupyter Notebook

## Pasos del análisis
* Creación del repositorio. Creamos el archivo gitignore para controlar que archivos y carpetas queremos que se suban.
* Creación del sistema de carpetas:
    * data: carpeta donde tenemos el fichero con el que vamos a trabajar.Contiene:
        * data-clean.csv

    * data\orig: carpeta donde guardamos los ficheros originales. Contiene:
        * bank-additional.csv
        * customer-details.xlsx  

    * data\transformados: carpeta donde guardamos los ficheros transformados. Contiene:  
        * bank-customers-detail.csv
    * jupyter: Guardamos los archivos de jupyter notebook utilizados durante el proceso. Contiene:
        * 1-EDA_preliminar.ipynb
        * 2-limpieza.ipynb
        * 3-columnas_categoricas.ipynb
        * 4-columnas_numericas.ipynb
        * 5-marketing.ipynb

    * src: guardamos los archivos de soporte de python con las funciones que hemos utilizado en el análisis.  
* Creación del entorno: Creamos un entorno exclusivo para el proyecto para gestionar las líbrerías y sus versiones.  






* Creamos el archivo '2-limpieza.ipynb' para realizar la limpieza y transformación de datos sobre el archivo data\transformados\bank-customers-detail.csv.  
 
    * Guardamos el fichero en un nuevo archivo 'bank-customers-clean.csv' en la carpeta data.  

* Dentro de la carpeta 'src' creamos un archivo de soporte llamado 'sp_limpieza.py' donde creamos todas las funciones utilizadas en el archivo 'limpieza.ipnyb'.

* Creamos el archivo '3-columnas_categoricas.ipynb' donde realizamos el análisis de las columnas categóricas y su gestión de los valores nulos.
    * En la columna 'loan', hemos rellenado los valores nulos con el valor 'No', al tener un 80% el valor 'no' y tener un 2.38% de valores nulos. La columna 'default' no la hemos tenido en cuenta al tener un 20.88% de valores nulos. La columna 'housing' tiene el mismo porcentage de valores nulos que 'loan', pero ninguna categoría predominante.
    * El resto de columnas, hemos creado una categoría nueva para los valores nulos: 'Unknown'. 

* Creamos el archivo de soporte llamado 'sp_analisis.py' donde creamos todas las funciones utilizadas en el análisi del archivo 'columnas_categoricas.ipnyb'.
* Creamos el archivo de soporte llamado 'sp_visualizacion.py' donde creamos todas las funciones utilizadas para visualizar gráficos del archivo 'columnas_categoricas.ipnyb'.

* Creamos el archivo '4-columnas_numericas.ipynb' donde realizamos el análisis de las columnas categóricas y su gestión de los valores nulos.  
    * Hemos visto la presencia de outliers en las columnas 'age', 'duration_min', 'campaign', 'pdays', 'previous', 'cons_conf_idx' a través de los histogramas y los diagramas de caja.
        * No vamos a eliminar nungún registro de las columnas con outliers. El número de registros y el porcentaje de los outliers no justifica su eliminación o canvio de valor.
    * Analizamos los valores nulos. Los dividimos en dos grupos:  
        1- Columnas por debajo del umbral del 5%, donde utilizamos el método fillna:
        - cons_price_idx: con outliers y valores no uniformes. Valores similares entre media y mediana. Rellenamos nulos con la media.
        - contact_year: no tiene outliers, distribución uniforme, valores similares entre media y mediana. Utilizamos la  mediana, al ser un año no podemos tener decimales.
        - contact_month: no tiene outliers, distribución uniforme, valores similares entre media y mediana. Utilizamos la  mediana, al ser un año no podemos tener decimales.

        2- Columnas por encima del umbral del 5%, donde utilizamos los métodos iterative imputer y knn imputer:
        * Nos quedaremos con los valores del knn
          - age: la mediana del knn se acerca más a la mediana original, y la media se desvía un poco más que la del iterative, pero no mucho. Nos quedaremos con los valores del knn.
          - euribor3m: la media del iterative es igual que la media del original. La mediana se acerca más la del knn.
        
        
* Modificamos el archivo de soporte llamado 'sp_analisis.py' donde creamos las funciones necesarias para la gestión de nulos de las columnas numéricas.        
* Modificamos el archivo de soporte llamado 'sp_visualizacion.py' donde creamos todas las funciones utilizadas para visualizar gráficos del archivo 'columnas_numericas.ipnyb'.

* Creamos el archivo '5-marketing.ipynb' para crear nueva métricas.
    * Métricas nuevas:
        - Tasa de resolución del primer contacto (FCR): Cuantos clientes han contratado en el primer contacto.
    * Analizamos las gráficas de las nuevas columnas para ver la presenciade outliers y la distribución de los datos.


## Conclusiones
La campaña de marketing ha sido mala. Solamente han conseguido captar el 11% de clientes a los que han contactado, de los cuales el 5% fueron en la primera llamada.
El perfil de personas que han contrado servicios es:
    - Estudiantes y parados.
    - Analfabetos.
    - Ya habían contratado un servicio con el banco anteriormente.
    - Edad entre 30-40 años

El tipo de contacto más efectivo a sido a través del movil.
Parece que no se han enfocado al público correcto. 


