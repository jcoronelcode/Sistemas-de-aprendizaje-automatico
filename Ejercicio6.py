import pandas as pd

datos = {
'Nombre': ['Ana', 'Juan', 'Pedro', 'Luis', 'Marta'],
'Edad': [23, 34, 45, 29, 30],
'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Bilbao', 'Valencia'],
'Salario': [2200, 3400, 4500, 2900, 3000]
}

df = pd.DataFrame(datos)
#1. Ordena el DataFrame por la columna "Salario" en orden descendente.
df = df.sort_values(by='Salario', ascending=True)
print(df)
print('**********************************')
#2. Filtra el DataFrame para mostrar solo las filas donde el "Salario" sea mayor de 3000.
print(df[df['Salario'] > 3000])