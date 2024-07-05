import pandas as pd

# Leer el archivo Parquet
df = pd.read_parquet('business.parquet')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Mostrar información sobre las columnas y tipos de datos
print(df.info())