import pandas as pd

# Ejercicio 10: Guardar y exportar datos
# 1. Guarda el DataFrame df creado en el ejercicio 1 en un archivo CSV llamado salarios.csv.
datos = {
'Nombre': ['Ana', 'Juan', 'Pedro', 'Luis', 'Marta'],
'Edad': [23, 34, 45, 29, 30],
'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Bilbao', 'Valencia'],
'Salario': [2200, 3400, 4500, 2900, 3000]
}

df = pd.DataFrame(datos)
df.to_csv('salarios.csv')
# 2. Guarda el DataFrame en formato Excel usando to_excel().
df.to_excel('salarios.xlsx')