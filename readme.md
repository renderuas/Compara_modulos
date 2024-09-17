

# Comparador de Módulos en Archivos CSV

Este script compara dos archivos CSV y encuentra los módulos coincidentes en base al nombre del módulo (`modulo_nombre`). Para cada coincidencia, se muestra el `id_agente_modulo` correspondiente de ambos archivos. El resultado también puede ser exportado a un archivo CSV.

## Requisitos

Para ejecutar este script, asegúrate de tener instalados los siguientes paquetes de Python:

- `pandas`

Si no lo tienes instalado, puedes hacerlo ejecutando:

```bash
pip install pandas
```
Uso
1. Cargar los archivos CSV

El script comparar_modulos.py toma dos archivos CSV como entrada, los cuales deben tener al menos las siguientes columnas:

    id_agente_modulo
    modulo_nombre

El archivo de origen puede tener más columnas, pero solo se utilizarán las mencionadas para la comparación.
2. Ejecución del script

Para ejecutar el script, simplemente llama a la función comparar_modulos con los nombres de los dos archivos CSV como parámetros.

python

comparar_modulos('origen.csv', 'comparacion.csv')

Esto mostrará en la salida estándar una tabla con los módulos coincidentes y los respectivos id_agente_modulo de cada archivo.
3. Guardar el resultado en un archivo CSV (Opcional)

Si deseas guardar el resultado de la comparación en un nuevo archivo CSV, puedes descomentar la línea siguiente en el script:

python

merged_df.to_csv('modulos_coincidentes.csv', index=False, sep=',')

Esto creará un archivo modulos_coincidentes.csv con los módulos coincidentes.
4. Ejemplo de salida

La salida de la función se verá así en la consola:

```mathematica

            modulo_nombre  id_agente_modulo_origen  id_agente_modulo_comparacion
0          Memory Free %                   19919                         99895
1           DiskFree%_C:                   19926                         99107
2           DiskFree%_E:                   19927                         99108
3           TOP Procesos                   98828                         99102
4           WMI Service                    98830                         99104
```
5. Parámetros

    origen.csv: El archivo CSV de origen que contiene los datos originales.
    comparacion.csv: El archivo CSV de comparación que contiene los datos que se van a comparar con el archivo de origen.

6. Nota sobre el formato de los archivos CSV

El script espera que los archivos CSV utilicen un separador de espacios o un delimitador adecuado que puede ser ajustado en el código. Actualmente, el delimitador está configurado para espacios usando:

```python

sep='\\s+'
```
Si tus archivos CSV utilizan otro delimitador (como comas o tabulaciones), puedes ajustar el parámetro sep en las llamadas a pd.read_csv.
Licencia

Este proyecto está bajo la licencia MIT. Puedes consultar el archivo LICENSE para más detalles.

