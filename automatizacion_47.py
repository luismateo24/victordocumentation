# ============================================
# AUTOMATIZACIÓN - Bot de Ventas
# ============================================
import time
import os
import pandas as pd
import glob
import matplotlib.pyplot as plt

# Se ajusta a tu carpeta "datos"
ruta_datos = "datos"

# Asegurar que la carpeta de resultados exista
if not os.path.exists("resultados"):
    os.makedirs("resultados")

archivos_vistos = set(os.listdir(ruta_datos))

def procesar_todo(archivo_nuevo):
    """
    Lee todos los archivos de sucursales en 'datos/', los consolida, 
    limpia duplicados, genera un gráfico de ventas por categoría
    y guarda un registro (log) del proceso.
    """
    archivos_csv = glob.glob(os.path.join(ruta_datos, "sucursal_*.csv"))
    archivos_xlsx = glob.glob(os.path.join(ruta_datos, "sucursal_*.xlsx"))
    
    lista_informes = []
    
    for archivo in archivos_csv:
        lista_informes.append(pd.read_csv(archivo))
    for archivo in archivos_xlsx:
        lista_informes.append(pd.read_excel(archivo, engine='openpyxl'))
    
    if not lista_informes:
        print("No se encontraron archivos de sucursales para procesar.")
        return

    df_consolidado = pd.concat(lista_informes, ignore_index=True)
    df_consolidado = df_consolidado.drop_duplicates()
    df_consolidado.to_excel("resultados/consolidado_limpio.xlsx", index=False)
    
    ventas_categoria = df_consolidado.groupby('categoria')['precio_unitario'].sum()
    ventas_categoria.plot(kind='bar', title='Ventas por Categoría')
    plt.ticklabel_format(style='plain', axis='y')
    plt.ylabel('Ventas totales (COP)')
    plt.tight_layout()
    plt.savefig("resultados/grafico_categoria.png")
    plt.close()
    
    with open("resultados/log_automatizacion.txt", "a", encoding="utf-8") as f:
        f.write(f"Proceso ejecutado: {pd.Timestamp.now()}\n")
        f.write(f"Archivo detectado: {archivo_nuevo}\n")
        f.write(f"Total de registros procesados: {len(df_consolidado)}\n")
        f.write("---\n")
    
    print(f"✅ Proceso completado - Archivo {archivo_nuevo} procesado correctamente.")


print("Monitoreando carpeta de datos... (Ctrl+C para detener)")

while True:
    archivos_actuales = set(os.listdir(ruta_datos))
    archivos_nuevos = archivos_actuales - archivos_vistos
    
    if archivos_nuevos:
        print(f"Nuevo archivo detectado: {archivos_nuevos}")
        for nuevo in archivos_nuevos:
            procesar_todo(nuevo)
        archivos_vistos = archivos_actuales
    
    time.sleep(5)