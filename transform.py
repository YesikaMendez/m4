import pyarrow.parquet as pq
import pandas as pd

# Especifica el nombre del archivo Parquet con su extensión
parquet_file = 'business.parquet'
# Especifica el nombre del archivo JSON de salida
json_file = 'output.json'

try:
    # Leer el archivo Parquet
    tbl = pq.read_table(parquet_file)
    df = tbl.to_pandas()

    # Convertir el DataFrame a JSON donde cada fila es un objeto JSON
    j = df.to_json(orient='records')

    # Escribir el JSON a un archivo
    with open(json_file, 'w') as f:
        f.write(j)

    print(f'Transformación completada. Archivo JSON guardado en: {json_file}')
except FileNotFoundError as e:
    print(f"Archivo no encontrado: {e}")
except Exception as e:
    print(f"Error al leer el archivo Parquet: {e}")
