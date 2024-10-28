import pandas as pd

datos = {
'Nombre': ['Ana', 'Juan', 'Pedro', 'Luis', 'Marta'],
'Edad': [23, 34, 45, 29, 30],
'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Bilbao', 'Valencia'],
'Salario': [2200, 3400, 4500, 2900, 3000]
}

df = pd.DataFrame(datos)
print(df)
print('********************************************')
# 1. Usando el DataFrame df, crea una nueva columna llamada Salario_Anual que multiplique el salario
# mensual por 12.
df['Salario_Anual'] = df['Salario'].apply(lambda x: x*12)
print(df)
# 2. Usa una función lambda para crear una nueva columna llamada Rango_Edad que sea:
# - "Joven" si la edad es menor a 30.
# - "Adulto" si la edad está entre 30 y 40.
# - "Mayor" si la edad es mayor a 40.
df['Rango_Edad'] = df['Edad'].apply(lambda x: 'Joven' if x < 30 else 'Adulto' if x >= 30 and x <= 40 else 'Mayor')
print(df)

