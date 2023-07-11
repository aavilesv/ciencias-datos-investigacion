
import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('estudiantes.xlsx')

# Agrupar por 'nombre' y sumar 'cantidad'
resultado = df.groupby('nombre')['cantidad'].sum().reset_index()
# Mostrar el resultado
# Guardar el resultado en un nuevo archivo Excel
resultado.to_excel('nuevoestudiantes.xlsx', index=False)