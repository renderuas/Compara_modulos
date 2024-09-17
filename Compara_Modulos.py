import pandas as pd

# Función para cargar los CSV y formatear los resultados
def comparar_modulos(origen_csv, comparacion_csv):
    # Cargar los ficheros CSV, usando un delimitador adecuado si es necesario
    origen_df = pd.read_csv(origen_csv, sep='\\s+', engine='python')
    comparacion_df = pd.read_csv(comparacion_csv, sep='\\s+', engine='python')

    # Limpiar los módulos de HTML encoding
    origen_df['modulo_nombre'] = origen_df['modulo_nombre'].replace({'&#x20;': ' ', '&#40;': '(', '&#41;': ')', '&gt;': '>'}, regex=True)
    comparacion_df['modulo_nombre'] = comparacion_df['modulo_nombre'].replace({'&#x20;': ' ', '&#40;': '(', '&#41;': ')', '&gt;': '>'}, regex=True)

    # Hacer un merge para encontrar los módulos coincidentes
    merged_df = pd.merge(
        origen_df[['id_agente_modulo', 'modulo_nombre']],
        comparacion_df[['id_agente_modulo', 'modulo_nombre']],
        on='modulo_nombre',
        suffixes=(f'_{origen_csv}', f'_{comparacion_csv}')
    )

    # Renombrar columnas dinámicamente según los archivos de entrada
    merged_df.rename(columns={
        f'id_agente_modulo_{origen_csv}': f'id_agente_modulo_{origen_csv.split(".")[0]}',
        f'id_agente_modulo_{comparacion_csv}': f'id_agente_modulo_{comparacion_csv.split(".")[0]}'
    }, inplace=True)

    # Imprimir el resultado
    print(merged_df[['modulo_nombre', f'id_agente_modulo_{origen_csv.split(".")[0]}', f'id_agente_modulo_{comparacion_csv.split(".")[0]}']])

    # guardar el resultado en CSV
    # merged_df.to_csv('modulos_coincidentes.csv', index=False, sep=',')

# Llamada a la función con los nombres de los archivos CSV
comparar_modulos('origen.csv', 'comparacion.csv')
