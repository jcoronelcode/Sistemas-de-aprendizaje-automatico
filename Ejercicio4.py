import pandas as pd

datos_ventas = {
    'Vendedor': ['Ana', 'Juan', 'Ana', 'Luis', 'Juan', 'Marta'],
    'Producto': ['PC', 'Laptop', 'Monitor', 'Teclado', 'Monitor', 'PC'],
    'Ventas': [1000, 1500, 800, 600, 900, 1100]
    }

ventas = pd.DataFrame(datos_ventas)

print(ventas)
print('******************************')
#Agrupa los datos por vendedor y calcula el total de las ventas de cada uno
ventas_vendedor = ventas.groupby('Vendedor').sum()
#Agrupa los datos por "Producto" y calcula el promedio de ventas para cada producto.
ventas_producto = ventas.groupby('Producto')['Ventas'].mean()
print(ventas_vendedor)
print('******************************')
print(ventas_producto)