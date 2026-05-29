# Proyecto: Análisis de Ventas

Este es un proyecto sencillo en Python para llevar el control de las ventas de materiales de construcción. 
El sistema lee un archivo con los datos de las transacciones, suma todas las unidades vendidas y guarda el resultado final en un informe de texto.

## 📁 Carpetas del Proyecto

* **`datos/`**: Aquí guardamos el archivo `ventas.csv` con todo el registro de los productos vendidos.
* **`scripts/`**: Acá está el código de Python (`ventas-totales.py`) que hace la magia y calcula las sumas.
* **`resultados/`**: En esta carpeta el programa guarda automáticamente el reporte final (`cantidad_total.txt`).

Pasos para reproducir el proyecto de forma local:

Debe verificar que tiene Python 3 instalado. Abra la terminal de su computadora o el símbolo del sistema en Windows y ejecute el comando python --version

Clonar el proyecto desde GitHub en su computadora: ejecute el comando git clone https://github.com/jeremiasjuarezREPO/Proyecto-Analisis-de-Ventas.git

Ingresar a la carpeta del repositorio que se acaba de descargar: cd Proyecto-Analisis-de-Ventas

Ejecutar el script de análisis desde la raíz del proyecto utilice el comando python scripts/ventas-totales.py

Al finalizar el último comando el programa leerá de forma automática el archivo datos/ventas.csv e imprimirá en su pantalla el mensaje de éxito indicando que el proceso terminó correctamente

El sistema creará de forma automática una carpeta llamada resultados si es que todavía no existe en su computadora y guardará allí un archivo de texto llamado cantidad_total.txt con la suma total de las unidades vendidas

---
