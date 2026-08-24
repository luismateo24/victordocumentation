import glob
import matplotlib.pyplot as plt
import pandas as pd

# ============================================
# PARTE 1: Buscar y leer los archivos
# ============================================
archivos_csv = glob.glob("datos/sucursal_*.csv")
archivos_xlsx = glob.glob("datos/sucursal_*.xlsx")
lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)
    print(f"Leído CSV: {archivo} - {len(df)} filas")

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo, engine="openpyxl")
    lista_informes.append(df)
    print(f"Leído XLSX: {archivo} - {len(df)} filas")


# ============================================
# PARTE 2 Y 3: Renombrar columnas distintas
# ============================================
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

# Consolidar archivos en un solo DataFrame
df_consolidado = pd.concat(lista_informes, ignore_index=True)
print(f"\nColumnas consolidadas ({len(df_consolidado.columns)}):")
print(list(df_consolidado.columns))


# ============================================
# PARTE 4: Limpieza de datos
# ============================================
filas_antes = len(df_consolidado)

# 1. Quitar espacios sobrantes en textos
for col in df_consolidado.select_dtypes(include="object").columns:
    df_consolidado[col] = df_consolidado[col].astype(str).str.strip()

# 2. Eliminar nulos y duplicados
df_consolidado = df_consolidado.dropna().drop_duplicates()

print(
    f"Filas antes de limpieza: {filas_antes} | Después de limpieza: {len(df_consolidado)}"
)


# ============================================
# PARTE 5: Guardar el resultado limpio
# ============================================
df_consolidado.to_excel("resultados/consolidado_limpio.xlsx", index=False)
print("✔ Archivo 'resultados/consolidado_limpio.xlsx' guardado con éxito.")


# ============================================
# PARTE 6: Análisis y Visualización
# ============================================

# 6a. Gráfico de Barras: Ventas totales por categoría
ventas_por_categoria = df_consolidado.groupby("categoria")[
    "precio_unitario"
].sum()
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(kind="bar", color="skyblue")
plt.title("Ventas por Categoría")
plt.ticklabel_format(style="plain", axis="y")  # Evita notación científica
plt.ylabel("Ventas totales ($)")
plt.xlabel("Categoría")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("resultados/grafico_ventas_categoria.png")
plt.show()

# 6b. Gráfico de Torta: Participación por vendedor
ventas_por_vendedor = df_consolidado.groupby("vendedor")[
    "precio_unitario"
].sum()
plt.figure(figsize=(7, 7))
ventas_por_vendedor.plot(
    kind="pie", autopct="%1.1f%%", title="Participación de Ventas por Vendedor"
)
plt.ylabel("")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas_vendedor.png")
plt.show()

# 6c. Producto más frecuente (Análisis con value_counts)
conteo_productos = df_consolidado["producto"].value_counts()
print("\n--- Conteo de ventas por producto ---")
print(conteo_productos)

# Gráfico de barras para los productos más vendidos
plt.figure(figsize=(9, 5))
conteo_productos.plot(kind="bar", color="orange")
plt.title("Frecuencia de Ventas por Producto")
plt.ylabel("Cantidad de Registros de Venta")
plt.xlabel("Producto")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("resultados/grafico_productos_frecuencia.png")
plt.show()