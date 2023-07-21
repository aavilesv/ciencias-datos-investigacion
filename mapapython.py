import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Lee la imagen del icono en un array de numpy
icon = mpimg.imread('C:\\Users\\AAVILESV\\Downloads\\locali.png') 

# Cargar el conjunto de datos mundial de Natural Earth incluido en GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
df = pd.read_excel('C:\\Users\\AAVILESV\\Downloads\\Agrupar python\\pais.xlsx')

# Asegúrate de que los nombres de las columnas sean 'country' y 'value'
df.columns = ['country', 'value']

# Puedes combinar 'df' con 'world' de la siguiente manera:
world = world.set_index('name').join(df.set_index('country'))
world['coords'] = world['geometry'].apply(lambda x: x.representative_point().coords[:])
world['coords'] = [coords[0] for coords in world['coords']]

fig, ax = plt.subplots(1, 1, figsize=(24, 18))

# Seleccionar los 5 países con los valores más altos
top_countries = df.nlargest(5, 'value')

# Añadir los valores de producción científica en el mapa
for idx, row in world.loc[top_countries['country']].iterrows():
    ax.annotate(text=str(idx).title() + ": " + str(int(row['value'])), xy=row['coords'], horizontalalignment='center', fontsize=12, weight='bold')


# ARREGLAR ESTE CÓDIGO YA QUE NO INGRESA EL ÍCONO Dibuja la imagen en las coordenadas de los países que no están en los 5 principales
for idx, row in world.loc[~world.index.isin(top_countries['country'])].iterrows():
    ax.imshow(icon, extent=(row['coords'][0]-0.1, row['coords'][0]+0.1, row['coords'][1]-0.1, row['coords'][1]+0.1))

# Usamos 'nipy_spectral' como colormap y normalizamos los valores para que estén entre 0 y 1
world['value_norm'] = (world['value'] - world['value'].min()) / (world['value'].max() - world['value'].min())
world.plot(column='value_norm', cmap='nipy_spectral', linewidth=0.8, edgecolor='0.8', alpha=0.4, legend=True, missing_kwds={'color': 'lightgrey'}, ax=ax)

# Añadir un título
plt.title('Scientific production of the countries')

# Mostrar el mapa
plt.show()
