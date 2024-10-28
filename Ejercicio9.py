import pandas as pd

datos_ventas_mes = {
'Mes': ['Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo'],
'Vendedor': ['Ana', 'Ana', 'Ana', 'Juan', 'Juan', 'Juan'],
'Ventas': [1000, 1500, 1100, 900, 1200, 1300]
}

df_ventas_mes = pd.DataFrame(datos_ventas_mes)
print(df_ventas_mes)
print('******************************************')
# 1. Usa pivot para reorganizar el DataFrame de modo que las columnas sean los meses y las filas los
# vendedores, con las ventas como valores.
df_pivot = df_ventas_mes.pivot(index='Vendedor', columns='Mes', values='Ventas')
print(df_pivot)
print('******************************************')
# 2. Usa melt para transformar el DataFrame de vuelta al formato largo.
df_melt = df_pivot.melt(value_name='Ventas').reset_index()
print(df_melt)