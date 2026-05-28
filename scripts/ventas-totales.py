import csv
import os

#Buscamos la carpeta donde esta guardado este script de Python
carpeta_actual = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'

#Subimos un nivel para salir de scripts y encontrar datos y resultados
carpeta_raiz = os.path.dirname(carpeta_actual)

#Armamos las rutas de los archivos usando el modulo os
ruta_entrada_csv = os.path.join(carpeta_raiz, 'datos', 'ventas.csv')
carpeta_salida_resultados = os.path.join(carpeta_raiz, 'resultados')
ruta_salida_txt = os.path.join(carpeta_salida_resultados, 'cantidad_total.txt')

#Variable acumuladora para ir sumando las unidades
total_unidades_vendidas = 0

#Abrimos el archivo de datos para leerlo fila por fila
with open(ruta_entrada_csv, mode='r', encoding='utf-8') as mi_archivo_csv:
    #Convertimos el archivo en un diccionario facil de leer
    lector_datos = csv.DictReader(mi_archivo_csv)
    
    #Ciclo for recorre cada fila del archivo ventas.csv
    for mi_fila in lector_datos:
        # Sacamos el valor de la columna y lo transformamos en un numero entero
        unidades_fila = int(mi_fila['cantidad vendida'])
        # Sumamos el valor al total acumulado
        total_unidades_vendidas = total_unidades_vendidas + unidades_fila

#Nos aseguramos de que la carpeta de resultados exista en el sistema
os.makedirs(carpeta_salida_resultados, exist_ok=True)

#Abre el archivo de texto para escribir el resultado final
with open(ruta_salida_txt, mode='w', encoding='utf-8') as mi_archivo_txt:
    # Escribimos el mensaje con el total calculado
    mi_archivo_txt.write(f"Cantidad total vendida: {total_unidades_vendidas}\n")

#Mostramos un mensaje en la pantalla para saber que todo salio bien
print("Proceso terminado con exito. El archivo txt fue guardado en resultados.")
