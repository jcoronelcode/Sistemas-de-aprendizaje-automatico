import pandas as pd

datos_nulos = {
'Nombre': ['Ana', 'Juan', 'Pedro', 'Luis', 'Marta'],
'Edad': [23, 34, None, 29, 30],
'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', None, 'Valencia'],
'Salario': [2200, None, 4500, 2900, 3000]
}

df = pd.DataFrame(datos_nulos)

print(df)
print('*********************************')
#2. Rellena los valores nulos de la columna "Salario" con el valor promedio de esa columna.
df['Salario'] = df['Salario'].fillna(df['Salario'].mean())
#3. Elimina las filas que contengan valores nulos en la columna "Ciudad".
df = df.dropna(subset=['Ciudad'])
#4. Rellena los valores nulos de la columna "Edad" con el valor anterior (método ffill).
df['Edad'] = df['Edad'].ffill()

print(df)