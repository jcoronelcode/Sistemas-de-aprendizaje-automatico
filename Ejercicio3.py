import pandas as pd

df_empleados = pd.read_csv('empleados.csv')


salario = df_empleados['Salario']
edadMas30 = df_empleados[df_empleados['Edad'] > 30]
# Selecciona las filas donde "Años en la empresa" sea 3 o 4.
anios = df_empleados[(df_empleados['Años en la empresa'] >= 3) & (df_empleados['Años en la empresa'] <= 8)]


print(anios)
# Salto de linea de 5 espacios
print("\n" * 5)
print(df_empleados)
# print(salario)
# print(edadMas30)