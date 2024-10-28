import pandas as pd

empleados1 = pd.DataFrame({
'EmpleadoID': [1, 2, 3],
'Nombre': ['Ana', 'Juan', 'Pedro'],
'Salario': [3000, 4000, 5000]
})

empleados2 = pd.DataFrame({
'EmpleadoID': [3, 4, 5],
'Nombre': ['Pedro', 'Luis', 'Marta'],
'Salario': [5000, 2500, 3500]
})

print(empleados1)
print(empleados2)
print('*************************************')
# 1. Realiza un merge de los DataFrames usando la columna "EmpleadoID" como clave.
resultado = pd.merge(empleados1, empleados2, on='EmpleadoID')
print(resultado)
print('*************************************')
# 2. Haz una unión completa (outer join) y analiza el resultado.
resultado = pd.merge(empleados1, empleados2, on='EmpleadoID', how='outer')
print(resultado)