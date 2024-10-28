import pandas as pd
import numpy as np

np.random.seed(0)

datos_desafio = pd.DataFrame({
    'A': np.random.randint(1, 100, 10),
    'B': np.random.randint(1, 100, 10),
    'C': np.random.randint(1, 100, 10)
})

# 1. Normaliza los datos en cada columna restando la media y dividiendo por la desviación estándar.
datos_desafio_normalizado = (datos_desafio - datos_desafio.mean()) / datos_desafio.std()

# 2. Calcula el valor absoluto de la diferencia entre las columnas A y B, y guárdalo en una nueva columna llamada Diff_AB.
datos_desafio['Diff_AB'] = (datos_desafio['A'] - datos_desafio['B']).abs()

# 3. Reemplaza los valores de la columna C que sean mayores de 50 con el valor 50.
datos_desafio['C'] = datos_desafio['C'].apply(lambda x: 50 if x > 50 else x)

print(datos_desafio)
print(datos_desafio_normalizado)