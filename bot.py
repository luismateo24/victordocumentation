import pandas as pd
import glob 

#1. Buscar datos y leer archivos

df_medellin =pd.read_csv('sucursal_medellin.csv')
#print(df_medellin)

df_bogota =pd.read_excel("sucursal_bogota.xlsx")
#print(df_bogota.head(3))

#print(df_medellin.columns)
#print(df_bogota.columns)

archivos_csv = glob.glob("*.csv")
print(f"Archivos_csv {archivos_csv}")


archivo_xlxs = glob.glob("*.xlsx")
print(f"Archivos_xlsx {archivo_xlxs}")


#2.Guardar en una lista



lista_dataframes = []

for archivos in archivos_csv:
    df = pd.read_csv(archivos)
    lista_dataframes.append(df)
    print(f"Leído: {archivos} - {len(df)} filas")

for archivo in archivo_xlxs:
    df = pd.read_excel(archivo)
    lista_dataframes.append(df)
    print(f"Leído: {archivo} - {len(df)} filas")



