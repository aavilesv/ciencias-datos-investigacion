
import pandas as pd
df1 = pd.read_excel('datao.xlsx')


valores = ['Computer Science', 'Information Science', 'Technology', 'computacion de ciencias']# área o categoría a buscar
regex = r'^(.*\s)?(' + '|'.join(valores) + r')(\s.*)?$'# Esto sirve para buscar donde comienza o termina deben estar en el arreglo
df_filtradoarea = df1[df1['AREA'].str.split(';').apply(lambda x: any(pd.Series(x).str.contains(regex, case=False, na=False)))]# el split es para seperar la columna seleccionada



 
 
# Crear una lista con las palabras de interés
palabras = ['web', 'evaluation', 'evaluate']#filtrar por criterios

# Crear una función que verifica si una cadena de texto comienza, termina o contiene alguna de las palabras de interés
def contains_words(text):
    text = '' if pd.isnull(text) else text
    return pd.Series(text.split(';')).str.contains('|'.join([rf'\b{word}\b' for word in palabras]), case=False, na=False).any()

# Crear una función que verifica si una cadena de texto (no dividida) comienza, termina o contiene alguna de las palabras de interés
def contains_words_no_split(text):
    text = '' if pd.isnull(text) else text
    return pd.Series(text).str.contains('|'.join([rf'\b{word}\b' for word in palabras]), case=False, na=False).any()

# Aplicar la función a las columnas de interés
#df_filtrado = df_filtradoarea[df_filtradoarea[['Author Keywords', 'Keywords Plus']].applymap(contains_words).any(axis=1) | df_filtradoarea[['Title', 'Abs']].applymap(contains_words_no_split).any(axis=1)]
df_filtrado = df_filtradoarea[df_filtradoarea[['Author Keywords', 'Keywords Plus']].applymap(contains_words).any(axis=1) | df_filtradoarea[['Title']].applymap(contains_words_no_split).any(axis=1)]
df_filtrado.to_excel('dfresultado.xlsx', index=False)


