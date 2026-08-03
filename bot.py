import glob
import pandas as pd

# ==========================================
# 1. BUSCAR Y LEER ARCHIVOS
# ==========================================
archivos_csv = glob.glob("*.csv")
archivos_xlsx = glob.glob("*.xlsx")

print(f"Archivos CSV encontrados: {archivos_csv}") #imprimir los archivos tipo CSV
print(f"Archivos Excel encontrados: {archivos_xlsx}") #imprimir los archivos tipo Excel

#Definimos lista_informes como se indico en el classroom
lista_informes = []

#Lee los archivos CSV
for archivo in archivos_csv:
    if archivo == "consolidado.xlsx":
        continue
    try:
        df = pd.read_csv(archivo)
        lista_informes.append(df)
        print(f"Leído CSV: {archivo} - {len(df)} filas")
    except Exception as e:
        print(f"Error al leer {archivo}: {e}")

#Lee los archivos Excel
for archivo in archivos_xlsx:
    if archivo == "consolidado.xlsx":
        continue
    try:
        df = pd.read_excel(archivo, engine="openpyxl")
        lista_informes.append(df)
        print(f"Leído Excel: {archivo} - {len(df)} filas")
    except Exception as e:
        print(f"Error al leer {archivo}: {e}")


# ==========================================
# 2. RENOMBRAR COLUMNAS (template.py)
# ==========================================
# Bogotá es la única sucursal con nombres de columnas diferentes.
# Encontramos el DataFrame usando 'Fecha_Venta' y organizamos los nombres para que sean consistentes.
for i, df in enumerate(lista_informes):
    if "Fecha_Venta" in df.columns:
        lista_informes[i] = df.rename(
            columns={
                "Fecha_Venta": "fecha",
                "Producto": "producto",
                "Categoria": "categoria",
                "Cant": "cantidad",
                "Valor_Unitario": "precio_unitario",
                "Vendedor": "vendedor",
                "Pago": "metodo_pago",
            }
        )


# ==========================================
# 3. LIMPIEZA Y CONSOLIDACIÓN DE DATOS
# ==========================================
if lista_informes:
    # Consolidamos los DataFrames
    df_consolidado = pd.concat(lista_informes, ignore_index=True)

    # Quitamos los espacios en texto, valores nulos y filas duplicadas.
    for col in df_consolidado.select_dtypes(include="object").columns:
        df_consolidado[col] = df_consolidado[col].astype(str).str.strip()

    df_consolidado = df_consolidado.dropna().drop_duplicates()

    # Exportamos el archivo final
    df_consolidado.to_excel("consolidado.xlsx", index=False)

    print(
        f"\nProceso completado"
        f"\nTotal de columnas: {len(df_consolidado.columns)} {list(df_consolidado.columns)}"
        f"\nTotal de filas consolidadas sin duplicados: {len(df_consolidado)}"
    )
else:
    print("\nNo se encontraron datos para consolidar.")