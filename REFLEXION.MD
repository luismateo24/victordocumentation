# Reflexión del Proyecto

### 1. ¿Qué hace `os.listdir(ruta_datos)`?
Es una función del módulo `os` de Python que devuelve una lista con los nombres de todos los archivos y carpetas contenidos dentro del directorio especificado en `ruta_datos`. Permite iterar dinámicamente sobre los archivos (por ejemplo, archivos `.csv` o `.xlsx`) para procesarlos en lote.

### 2. ¿Qué diferencia hay entre `set` y `lista` para guardar archivos vistos?
* **Lista (`list`):** Mantiene el orden de inserción y permite elementos duplicados. Buscar si un archivo ya fue visto (`if archivo in lista`) tiene una complejidad $O(n)$, lo que se vuelve más lento a medida que crece la cantidad de elementos.
* **Conjunto (`set`):** Solo almacena elementos únicos (elimina duplicados automáticamente) y no garantiza un orden. Buscar un archivo (`if archivo in set_vistos`) tiene una complejidad $O(1)$, lo que hace la verificación prácticamente instantánea sin importar el tamaño del historial.

### 3. ¿Qué hace `drop_duplicates()` y por qué es importante aquí?
Es un método de Pandas que elimina las filas duplicadas de un DataFrame. En este sistema es fundamental para garantizar la **integridad e idoneidad de los datos**: evita procesar o consolidar registros repetidos provenientes de múltiples cargas de archivos, asegurando que los reportes finales y métricas sean precisos.

### 4. ¿Cuántos commits tiene tu repo? Menciona 2 de tus mensajes
*(Abre la terminal en tu proyecto y ejecuta `git rev-list --count HEAD` para obtener el número exacto, luego revisa con `git log --oneline`)*

* **Total de commits:** X commits.
* **Mensajes de ejemplo:**
  1. `feat: add data cleaning pipeline with drop_duplicates`
  2. `docs: update README with setup instructions`

### 5. ¿Qué mejora le harías a este sistema?
* **Validación de esquemas/columnas:** Implementar una verificación previa de las columnas esperadas en cada archivo antes de consolidarlos, notificando al usuario si un archivo tiene una estructura incorrecta.
* **Manejo de excepciones e historial persistente:** Guardar la lista de archivos ya procesados en una base de datos liviana (o un archivo `.json`/`.txt` persistente) para evitar reprocesar datos al reiniciar el script, además de registrar errores en un archivo de log (`logging`).

### 6. ¿Qué fue lo que más te gustó aprender?
Lo que más disfruté fue comprender la eficiencia de las estructuras de datos (como el uso de conjuntos en lugar de listas para búsquedas rápidas) y ver cómo Pandas automatiza en segundos la limpieza y consolidación masiva de datos que manualmente tomaría horas.