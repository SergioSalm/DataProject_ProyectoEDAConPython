import pandas as pd

def eda_preliminar (df):
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
    for col in lista_col:
            df[col] = df[col].str.replace(',','.')

def convertir_enteros(df):
    for col in df.columns:
        if df[col].dtype == 'O':
            for dtype in [float, int]:   
                try:
                    df[col] = df[col].astype(dtype)
                except:
                     pass       
        
def convertir_fechas(df, fecha_formato):
    for col, formato in fecha_formato.items():
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format=formato)
            



def convertir_YesNo(df, lista_col):
    for col in lista_col:
        df[col] = df[col].map({1:"yes", 0:"no"})
        df.loc[df[col].isnull(), col] = 'None'

