# Importar librerías principales y cargar el archivo local de Netflix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Mostrar una fracción de los datos para visualizar encabezados y algunos datos
csv_path = os.path.join(os.path.dirname(__file__), 'netflix_titles.csv')
df = pd.read_csv(csv_path)
print("Vista previa de los datos:")
print(df.head())

# 2. Limpiar datos vacíos (eliminar filas con valores nulos)
df = df.dropna()
print("\nDatos después de eliminar filas con valores vacíos:")
print(df.head())

# 3. Eliminar columnas no importantes para el análisis
# Selecciona solo las columnas relevantes para análisis general
columnas_utiles = ['type', 'title', 'country', 'release_year', 'rating', 'duration']
df = df[columnas_utiles]
print("\nDatos con columnas seleccionadas:")
print(df.head())

# 4a. Gráfica de barras: Top 10 países con más títulos
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.index, y=top_countries.values, palette='viridis')
plt.title('Top 10 países con más títulos en Netflix')
plt.ylabel('Cantidad de títulos')
plt.xlabel('País')
plt.xticks(rotation=45)
plt.show()

# 4b. Histograma: distribución de años de lanzamiento
plt.figure(figsize=(8,4))
df['release_year'] = df['release_year'].astype(int)
plt.hist(df['release_year'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de años de lanzamiento')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Frecuencia')
plt.show()

# 4c. Gráfica de cajas: duración de películas (en minutos)
# Extraer minutos de la columna 'duration' solo para películas
df_movies = df[df['type'] == 'Movie'].copy()
df_movies['duration_mins'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)
plt.figure(figsize=(8,3))
sns.boxplot(data=df_movies, x='duration_mins')  # Cambiado de y= a x=
plt.title('Duración de películas (minutos)')
plt.xlabel('Duración (min)')
plt.show()

# 4d. Gráfica de calor: títulos por año y rating
anios_filtrados = df['release_year'] >= 2000
pivot = df[anios_filtrados].pivot_table(
    index='rating', columns='release_year', values='title', aggfunc='count', fill_value=0
)
plt.figure(figsize=(12,6))
sns.heatmap(pivot, cmap='YlGnBu')
plt.title('Cantidad de títulos por año y rating (desde 2000)')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Rating')
plt.show()
