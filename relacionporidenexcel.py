import pandas as pd

# Leer los archivos Excel
df1 = pd.read_excel('docentesperu.xlsx')
df2 = pd.read_excel('matriculadosperu.xlsx')

# Unir los DataFrames basándote en la columna de ID
resultado = pd.merge(df1, df2, on='codigo')


'''
# Agrupar por 'nombre' y 'gestion_x', y sumar 'cantidaddocente' y 'cantidadestudiantes'
df = df.groupby(['nombre', 'gestion_x']).agg({'cantidaddocente': 'sum', 'cantidadestudiantes': 'sum'}).reset_index()

# Ordenar por 'nombre' y 'gestion_x'
df = df.sort_values(['nombre', 'gestion_x'])

# Guardar el resultado en un nuevo archivo Excel
resultado.to_excel('totalperu_.xlsx', index=False)'''