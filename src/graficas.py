import pandas as pd
import plotly.express as px
import os

# Lee tu archivo CSV
csv_path = os.path.join(os.path.dirname(__file__), '../data/netflix_titles.csv')
df = pd.read_csv(csv_path)

# Limpieza de datos
df = df.dropna()
columnas_utiles = ['type', 'title', 'country', 'release_year', 'rating', 'duration']
df = df[columnas_utiles]

# 1. Gráfica de barras: Top 10 países con más títulos
top_countries = df['country'].value_counts().head(10)
fig1 = px.bar(
    x=top_countries.index,
    y=top_countries.values,
    labels={'x': 'País', 'y': 'Cantidad de títulos'},
    title='Top 10 países con más títulos en Netflix'
)
fig1.update_layout(width=600, height=400)
fig1.write_html('plots/grafica1.html')

# 2. Histograma: distribución de años de lanzamiento
fig2 = px.histogram(
    df, x='release_year',
    nbins=20,
    title='Distribución de años de lanzamiento',
    labels={'release_year': 'Año de lanzamiento', 'count': 'Frecuencia'}
)
fig2.update_layout(width=600, height=400)
fig2.write_html('plots/grafica2.html')

# 3. Gráfica de cajas: duración de películas (en minutos)
df_movies = df[df['type'] == 'Movie'].copy()
df_movies['duration_mins'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)
fig3 = px.box(
    df_movies, x='duration_mins',
    title='Duración de películas (minutos)',
    labels={'duration_mins': 'Duración (min)'}
)
fig3.update_layout(width=600, height=400)
fig3.write_html('plots/grafica3.html')

# 4. Gráfica de calor: títulos por año y rating (desde 2000)
anios_filtrados = df['release_year'] >= 2000
pivot = df[anios_filtrados].pivot_table(
    index='rating', columns='release_year', values='title', aggfunc='count', fill_value=0
)
fig4 = px.imshow(
    pivot,
    labels=dict(x="Año de lanzamiento", y="Rating", color="Cantidad de títulos"),
    title='Cantidad de títulos por año y rating (desde 2000)'
)
fig4.update_layout(width=600, height=400)
fig4.write_html('plots/grafica4.html')