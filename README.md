# Proyecto EDA con Python

## Objetivo del proyecto
Este proyecto tiene como objetivo analizar los datos de una campaña de marketing de un banco portugués, para contratar un depósito a plazo bancario a través del análisis de los datos de la campaña de marketing y los datos demográficos de los clientes.
Buscaremos características comunes entre los clientes que han decidido subscribirse al producto y áreas de mejora, para optimizar las campañas futuras y mejorar la segmentación de la audencia.

## Descripción del conjunto de datos
Tenemos dos fichreos de datos:
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
    **pip install jupyter pandas numpy openpyxl**

    4. Creamos el archivo requeriments.txt para registrar las dependencias instaladas:  
    **pip freeze > requirements.txt**

* Creamos el archivo de jupyter 'EDA_preliminar.ipynb' para cargar y entender los datos con los que vamos a trabajar.
    * Analizamos los fichero:
        * bank-additional.csv   
            - Filas: 43.000  
            - Columnas: 24  
            - Tenemos 10 columnas con valores nulos.  
            - El tipo de datos de los valores de algunas columnas es incorrecto.
            - Cambiamos el nombre de las columnas
            - Eliminamos la columna unnamed:_0
            - Guardamos los cambios en un nuevo fichero en la carpeta data\transformados\bank-additional.csv  

        * customer-details.xlsx  
            Este fichero consta de 3 hojas  
            * Hoja 1
                - Filas: 20115
                - Columnas: 7  
            * Hoja 2
                - Filas: 8965
                - Columnas: 7  
            * Hoja 3
                - Filas: 14090
                - Columnas: 7  

            Las 3 hojas tienen las mismas columnas con el mismo nombre. Agrupamos las 3 hojas en un solo dataframe.
            - Las columnas no tienen valores nulos.  
            - El tipo de datos de los valores de las columnas es correcto.

            - Cambiamos el nombre de las columnas
            - Renombramos la columna ID a id_
            - Eliminamos la columna unnamed:_0
            - Guardamos los cambios en un nuevo fichero en la carpeta data\transformados\bank-additional.csv



    
* Unimos los dos ficheros en un único fichero final llamado bank-customer.csx en la carpeta data.

