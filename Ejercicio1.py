import pandas

datos = {
'Nombre': ['Ana', 'Juan', 'Pedro', 'Luis', 'Marta'],
'Edad': [23, 34, 45, 29, 30],
'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Bilbao', 'Valencia'],
'Salario': [2200, 3400, 4500, 2900, 3000]
}

df = pandas.DataFrame(datos)
# Mostrar las primeras 3 filas
print(df.head(3))
# Mostrar las últimas 2 filas
print(df.tail(2))

print(df.describe())