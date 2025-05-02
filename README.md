# Proyecto EDA con Python

## Objetivo del proyecto
Este proyecto tiene como objetivo analizar los datos de una campaña de marketing de un banco portugués, para contratar un depósito a plazo bancario a través del análisis de los datos de la campaña de marketing y los datos demográficos de los clientes.
Buscaremos características comunes entre los clientes que han decidido subscribirse al producto y áreas de mejora, para optimizar las campañas futuras y mejorar la segmentación de la audencia.

## Descripción del conjunto de datos
El cliente no pasa un documento word donde nos indica que tenemos dos fichreos de datos:
1. bank-additional.csv  
    * Resumen de las columnas:
        * **age:** La edad del cliente.
        * **job:** La ocupación o profesión del cliente.
        * **marital:** El estado civil del cliente.
        * **education:** El nivel educativo del cliente.
        * **default:** Indica si el cliente tiene algún historial de incumplimiento de pagos (1: Sí, 0: No).
        * **housing:** Indica si el cliente tiene un préstamo hipotecario (1: Sí, 0: No).
        * **loan:** Indica si el cliente tiene algún otro tipo de préstamo (1: Sí, 0: No).
        * **contact:** El método de contacto utilizado para comunicarse con el cliente.
        * **duration:** La duración en segundos de la última interacción con el cliente.
        * **campaign:** El número de contactos realizados durante esta campaña para este cliente.
        * **pdays:** Número de días que han pasado desde la última vez que se contactó con el cliente durante esta campaña.
        * **previous:** Número de veces que se ha contactado con el cliente antes de esta campaña.
        * **poutcome:** Resultado de la campaña de marketing anterior.
        * **emp.var.rate:** La tasa de variación del empleo.
        * **cons.price.idx:** El índice de precios al consumidor.
        * **cons.conf.idx:** El índice de confianza del consumidor.
        * **euribor3m:** La tasa de interés de referencia a tres meses.
        * **nr.employed:** El número de empleados.
        * **y:** Indica si el cliente ha suscrito un producto o servicio (Sí/No).
        * **date:** La fecha en la que se realizó la interacción con el cliente.
        * **contact_month:** Mes en el que se realizó la interacción con el cliente durante la campaña de marketing.
        * **contact_year:** Año en el que se realizó la interacción con el cliente durante la campaña de marketing.
        * **id_:** Un identificador único para cada registro en el dataset.


2. customer-details.xlsx  
    * Resumen de las columnas:
        * **Income:** Representa el ingreso anual del cliente en términos monetarios.
        * **Kidhome:** Indica el número de niños en el hogar del cliente.
        * **Teenhome:** Indica el número de adolescentes en el hogar del cliente.
        * **Dt_Customer:** Representa la fecha en que el cliente se convirtió en cliente de la empresa.
        * **NumWebVisitsMonth:** Indica la cantidad de visitas mensuales del cliente al sitio web de la empresa.
        * **ID:** Identificador único del cliente.
    
Vemos dos errores en el documento sobre el fichero 'bank-additional.csv'
1. No existen las columnas 'contact_month', ni 'contact_year' en el fichero. 
2. Existen las columnas 'latitude' y 'longitude' que no están documentadas.

## Herramientas utilizadas
Python (Pandas, seaborn, matplotlib)
Jupyter Notebook

## Pasos del análisis
* Creación del repositorio. Creamos el archivo gitignore para controlar que archivos y carpetas queremos que se suban.
* Creación del sistema de carpetas:
    * data: carpeta donde tenemos el fichero con el que vamos a trabajar
    * data\orig: carpeta donde guardamos los ficheros originales. Contiene:
        * bank-additional.csv
        * customer-details.xlsx  

    * data\transformados: carpeta donde guardamos los ficheros transformados. Contiene:  
        * bank_additional.csv
    * jupyter: Guardamos los archivos de jupyter notebook utilizados durante el proceso. Contiene:
        * EDA_preliminar.ipynb: se han realiado procesos de transformación y limpieza.
    * src: guardamos los archivos de soporte de python con las funciones que hemos utilizado en el análisis.  
* Creación del entorno: Creamos un entorno exclusivo para el proyecto para gestionar las líbrerías y sus versiones.   
Pasos realizados a través del terminal:  
    1. Desde la carpeta del proyecto, creamos el entorno virtual:  
    **python3 -m venv venv**
  
    2. Activamos el entorno:  
    **source venv/Scripts/activate**

    3. Instalamos las líbrerías necesarias:  
    **pip install jupyter pandas numpy openpyxl matplotlib seaborn scikit-learn**

    4. Creamos el archivo requeriments.txt para registrar las dependencias instaladas:  
    **pip freeze > requirements.txt**

* Creamos el archivo de jupyter 'EDA_preliminar.ipynb' para cargar y entender los datos con los que vamos a trabajar.
    * Analizamos los fichero:
        * bank-additional.csv   
            - Filas: 43.000  
            - Columnas: 23  
            - Tenemos 10 columnas con valores nulos.  
            - El tipo de datos de los valores de algunas columnas es incorrecto.
            - Cambiamos el nombre de las columnas
            - Renombramos la columna id_ a id 

        * customer-details.xlsx  
            Este fichero consta de 3 hojas  
            * Hoja 1
                - Filas: 20115
                - Columnas: 6  
            * Hoja 2
                - Filas: 8965
                - Columnas: 6  
            * Hoja 3
                - Filas: 14090
                - Columnas: 6  

            Las 3 hojas tienen las mismas columnas con el mismo nombre. Agrupamos las 3 hojas en un solo dataframe.
            - Las columnas no tienen valores nulos.  
            - El tipo de datos de los valores de las columnas es correcto.
            - Cambiamos el nombre de las columnas
            - Renombramos la columna ID a id
            
    * Unimos los dos df en un único df llamado bank-customers-detail.csv en la carpeta data\transformados
        - Filas: 43.000  
        - Columnas: 28  

* Creamos el archivo limpieza.ipynb para realizar la limpieza y transformación de datos sobre el archivo data\transformados\bank-customers-detail.csv.  
    * Eliminamos las columnas 'latitude' y 'longitude'.
    * Convertimos todos los datos del dataframe a minúsculas para homogeneizar los datos.  
    * Sustituimos las "," por los puntos en las columnas 'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed'.  
    * Hacemos una conversión en la columna date, donde cambiamos el nombre del mes por el número correspondiente.  
    * Cambiamos el tipo de datos de las columnas de tipo fecha y de las columnas de tipo numéricas.
    * Cambiamos los valores 1, 0, nan por 'Yes', 'No', 'None' en las columnas 'default', 'housing' y 'loan'
    * En la columna pdays, cambiamos el valor 999 por -1, para tener los datos más agrupados.

    * Creamos las nuevas columnas:
        * contact_year: año de la interacción del banco con el cliente
        * contact_month: mes de la interacción del banco con el cliente
        * customer_year: año en el que se convirtió en cliente de la empresa.
        * customer_month: mes en el que se convirtió en cliente de la empresa.
        * Creamos la columna 'subscribed' para tener un título más aclarativo y borramos la columna original 'y'.  
        * Creamos la columna 'duration_min' para tener los tiempos de las llamadas en minutos y eliminamos la columna 'duration'.  
    * Guardamos el fichero en un nuevo archivo 'bank-customers-clean.csv' en la carpeta data.  

* Dentro de la carpeta 'src' creamos un archivo de soporte llamado 'sp_limpieza.py' donde creamos todas las funciones utilizadas en el archivo 'limpieza.ipnyb'.

* Creamos el archivo 'columnas_categoricas.ipynb' donde realizamos el análisis de las columnas categóricas y su gestión de los valores nulos.
    * En la columna 'loan', hemos rellenado los valores nulos con el valor 'No', al tener un 80% el valor 'no' y tener un 2.38% de valores nulos. La columna 'default' no la hemos tenido en cuenta al tener un 20.88% de valores nulos. La columna 'housing' tiene el mismo porcentage de valores nulos que 'loan', pero ninguna categoría predominante.
    * El resto de columnas, hemos creado una categoría nueva para los valores nulos: 'Unknown'. 

* Creamos el archivo de soporte llamado 'sp_analisis.py' donde creamos todas las funciones utilizadas en el análisi del archivo 'columnas_categoricas.ipnyb'.
* Creamos el archivo de soporte llamado 'sp_visualizacion.py' donde creamos todas las funciones utilizadas para visualizar gráficos del archivo 'columnas_categoricas.ipnyb'.

* Creamos el archivo 'columnas_numericas.ipynb' donde realizamos el análisis de las columnas categóricas y su gestión de los valores nulos.  
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




