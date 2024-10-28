import pandas as pd

df_empleados = pd.read_csv('numero-de-empleados.csv')

print(df_empleados.head(5))

# Verificar si hay valores nulos
print(df_empleados.isnull())

