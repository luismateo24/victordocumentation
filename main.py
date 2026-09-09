import glob
import os
import matplotlib.pyplot as plt
import pandas as pd

# Asegurar que existan las carpetas necesarias
os.makedirs("resultados", exist_ok=True)

# ============================================
# PARTE 1: Buscar y leer los archivos
# ============================================
archivos_csv = glob.glob("data/sucursal_*.csv")
archivos_xlsx = glob.glob("data/sucursal_*.xlsx")
lista_informes = []

for archivo in archivos_csv:
    # Soporte para encoding en lectura CSV
    df = pd.read_csv(archivo, encoding="utf-8")
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
plt.close()

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
plt.close()

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
plt.close()


# ============================================
# PARTE 7: Automatización, Registro de Log y Resumen Ejecutivo
# ============================================
def procesar_todo():
    # 1. Registro en el log (con encoding="utf-8")
    with open("resultados/log_automatizacion.txt", "a", encoding="utf-8") as log:
        log.write(
            f"[{pd.Timestamp.now()}] Procesamiento ejecutado exitosamente sobre {len(df_consolidado)} registros.\n"
        )

    # 2. Cálculo de Métricas requeridas e investigadas
    total_ventas = df_consolidado["precio_unitario"].sum()
    categoria_top = (
        df_consolidado.groupby("categoria")["precio_unitario"].sum().idxmax()
    )
    vendedor_top = (
        df_consolidado.groupby("vendedor")["precio_unitario"].sum().idxmax()
    )

    # Métricas adicionales solicitadas (investigadas):
    # - Producto más vendido (por frecuencia usando value_counts)
    producto_top = df_consolidado["producto"].value_counts().idxmax()
    # - Promedio de venta por transacción (usando mean)
    promedio_venta = df_consolidado["precio_unitario"].mean()

    # 3. Banner visual en pantalla
    print("\n" + "=" * 40)
    print("  NUEVO REPORTE PROCESADO EXITOSAMENTE")
    print(f"  Total ventas acumuladas: ${total_ventas:,.0f}")
    print("=" * 40 + "\n")

    # 4. Resumen ejecutivo en archivo de texto (con encoding="utf-8")
    with open("resultados/resumen_ejecutivo.txt", "w", encoding="utf-8") as f:
        f.write("RESUMEN EJECUTIVO - Bot de Ventas\n")
        f.write(f"Fecha: {pd.Timestamp.now()}\n\n")
        f.write(f"Categoría con mejor desempeño: {categoria_top}\n")
        f.write(f"Vendedor con más ventas: {vendedor_top}\n")
        f.write(f"Producto más vendido: {producto_top}\n")
        f.write(f"Promedio de venta por transacción: ${promedio_venta:,.2f}\n")
        f.write(f"Total de ventas acumuladas: ${total_ventas:,.0f}\n")

    print("Proceso completado...")


# Ejecución de la automatización
procesar_todo()