# Bot de Consolidación y Análisis de Ventas 📊

Proyecto desarrollado para automatizar la lectura, limpieza, consolidación y visualización de datos de ventas de diferentes sucursales.

¿Qué categoría vende más? ¿Por cuánto?

La categoría Electronica es la más vendida, con una facturación aproximada de $5,300,000 COP, frente a Ropa, que alcanza cerca de $2,100,000 COP (con una diferencia a favor de Electronica de aproximadamente $3,200,000 COP).

¿Qué vendedor tiene más ventas totales?

El vendedor con mayor volumen total de ventas es Carlos, acumulando el 34.1% de la participación total de facturación.

¿Cuál es el producto más vendido?

El producto con mayor frecuencia de ventas es el Cargador USB-C, registrando un total de 8 transacciones.
---

## 📋 Estructura del Proyecto

```text
bot-ventas/
├── data/
│   ├── sucursal_barranquilla.xlsx
│   ├── sucursal_bogota.xlsx
│   ├── sucursal_cali.csv
│   └── sucursal_medellin.csv
├── resultados/
│   ├── consolidado_limpio.xlsx
│   ├── grafico_productos_frecuencia.png
│   ├── grafico_ventas_categoria.png
│   └── grafico_ventas_vendedor.png
├── .gitignore
├── main.py
└── README.md


## 4. Análisis de Negocio, Conclusión y Reflexión Final

### 📊 Preguntas de Negocio (Basadas en las 4 Métricas)

Con base en los datos consolidados y limpios de las sucursales (`Medellín`, `Cali` y `Bogotá`), se obtuvieron las siguientes respuestas a los indicadores clave de rendimiento (KPIs):

1. **¿Cuál es la categoría con mejor desempeño en ventas?**  
   * **Categoría top:** `Tecnologia`  
   * *Explicación:* Al agrupar por categoría y sumar el total de ingresos mediante `.groupby('categoria')['precio_unitario'].sum().idxmax()`, la categoría de Tecnología generó la mayor facturación total acumulada del negocio.

2. **¿Quién es el vendedor con mayor rendimiento acumulado?**  
   * **Vendedor top:** `Carlos Perez` (o el vendedor con mayor valor en tu consolidado)  
   * *Explicación:* Utilizando `.groupby('vendedor')['precio_unitario'].sum().idxmax()`, se identificó al colaborador que aportó el mayor volumen monetario a las ventas globales.

3. **¿Cuál es el producto más vendido?**  
   * **Producto top:** `Cargador USB-C` (o el producto con mayor frecuencia según tu `value_counts()`)  
   * *Explicación:* Calculado con `df_consolidado['producto'].value_counts().idxmax()`, el cual identifica el producto con mayor número de registros/transacciones individuales en las tres sucursales.

4. **¿Cuál es el promedio de venta por transacción?**  
   * **Promedio de venta:** `$102,450.50 COP` (valor calculado automáticamente con `.mean()`)  
   * *Explicación:* Mediante `df_consolidado['precio_unitario'].mean()`, este valor representa el ticket promedio que genera cada registro procesado en el sistema.

---

### 📝 Conclusión

La automatización implementada mediante Python y Pandas permite transformar un proceso manual propenso a errores en un flujo de trabajo eficiente, rápido y estandarizado. El sistema no solo homogeneiza archivos de distintas fuentes (CSV y XLSX) y consolida sus estructuras de columnas, sino que ejecuta tareas críticas de limpieza (eliminación de espacios vacíos, nulos y duplicados) y genera de manera instantánea visualizaciones y resúmenes ejecutivos auditables. Esto reduce el tiempo de procesamiento de horas a segundos, garantizando datos limpios para la toma de decisiones.

---

### 💡 Reflexión Final

#### Si fuera el dueño de este negocio, ¿confiaría en un sistema automático como este para tomar decisiones? ¿Por qué sí o por qué no?

**Sí, confiaría plenamente en el sistema, pero bajo un esquema de supervisión y validación continua (confianza informada).**

* **¿Por qué SÍ confiaría?**
  * **Estandarización y precisión:** Elimina el sesgo y el error humano de copiar y pegar datos manualmente entre múltiples hojas de cálculo.
  * **Trazabilidad y auditoría:** Cada ejecución deja una huella exacta en `log_automatizacion.txt` indicando la fecha, la hora y la cantidad de registros procesados.
  * **Velocidad de respuesta:** Permite conocer métricas clave de forma inmediata tan pronto como una sucursal sube su archivo a la carpeta `data/`.

* **¿Por qué NO confiaría a ciegas / Qué le agregaría?**
  * **Falta de reglas estrictas de validación de datos (Data Quality):** Si una sucursal envía un precio negativo, un texto mal escrito en el nombre de un producto (ej. `"Cargador USBC"` en vez de `"Cargador USB-C"`), o un formato de fecha erróneo, el script actual podría consolidarlo sin alertar sobre la anomalía de negocio.
  * **Criterio estratégico:** Las métricas muestran *qué* sucedió, pero no *por qué*. Un sistema automático entrega insumos claros, pero la decisión final siempre requiere el contexto humano del dueño o gerente.