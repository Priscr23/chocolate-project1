import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('Cacao flavors project')
st.markdown('*priscila cervantes*')
st.header('Historia del cacao')
st.text("""El chocolate es originario de latinoamérica siendo México el primero
en cultivarlo, donde para los Mayas  era considerado un ”alimento de dioses ”, 
sirviendo como monedas la semilla de cacao.
La forma en como consumían el 'Xoclatl (del náhuatl)'  era con agua fría, semillas
de cacao tostadas y molidas, era líquido amargo, a veces picante y espumoso, 
mezclado con infinidad de especias o puré de maíz.
A la llegaada de Hernán Cortés hace 500 años fue él quien llevó este fruto y receta 
de nuestros antepasados a su rey, Carloos V., 20 años más tarde cambian la receta 
añadiéndole azúcar y calentando la bebida.
Con eso se fue expandiendo por toda europa; con la llegada de la Revolución industrial 
se modificó aún más convirtiendola a lo que hoy en día conocemos como el chocolalte 
en barra; así igual llegó mundialmente agregándole más ingredientes. """)
st.image('C:/Users/prisc/apps/chocolate-project1/data/raw/cacao.webp')
st.header('Data set')
df=pd.read_csv('C:/Users/prisc/apps/chocolate-project1/reports/streamlit\datos_modificados2.csv')
st.dataframe(df)
print('\n')
moda_bean = df['Bean type'].mode()[0]
plt.figure(figsize=(8, 6))
df['Bean type'].value_counts().plot(kind='bar',color='#A0522D')
plt.title('Frecuencia de Tipos de Frijoles')
plt.xlabel('Tipo de Frijol')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
st.pyplot()

# Mostrar la moda de los tipos de frijoles en Streamlit
st.write("La moda de los tipos de frijoles es:", moda_bean)
print('\n')
frecuencia_region = df['Broad region of origin of bean'].value_counts()
region_mas_comun = frecuencia_region.idxmax()
st.write("La región de origen más común de las semillas de cacao es:", region_mas_comun)
st.bar_chart(frecuencia_region, color='#D2691E')
print('\n')
frecuencia_ubicacion = df['Company location'].value_counts()
ubicacion_mas_comun = frecuencia_ubicacion.idxmax()
st.write("La ubicación más común de las compañías productoras de chocolate es:", ubicacion_mas_comun)
st.bar_chart(frecuencia_ubicacion, color='#6B4423')
print('\n')
calificacion_promedio_porcentaje = df.groupby('Cocoa %')['Rating'].mean()
calificacion_promedio_porcentaje = calificacion_promedio_porcentaje.sort_values()
porcentaje_mas_popular = calificacion_promedio_porcentaje.idxmax()
st.write("El porcentaje de cacao más popular es:", porcentaje_mas_popular)
st.bar_chart(calificacion_promedio_porcentaje, color='#8B4513')
print('\n')
calificacion_promedio_por_tipo = df.groupby('Bean type')['Rating'].mean()
max_rating = calificacion_promedio_por_tipo.max()
tipos_mas_puntuados = calificacion_promedio_por_tipo[calificacion_promedio_por_tipo == max_rating].index.tolist()
st.write("Los tipos de semilla de frijol con los mayores puntajes son:")
for tipo in tipos_mas_puntuados:
    st.write(tipo)
st.bar_chart(calificacion_promedio_por_tipo, color='#DAA520')
print('\n')
st.subheader('Mejor rating')
calificacion_promedio_por_compania = df.groupby('Company')['Rating'].mean()
mejor_compania = calificacion_promedio_por_compania.idxmax()
calificacion_promedio_maxima = calificacion_promedio_por_compania.max()
ubicacion_mejor_compania = df.loc[df['Company'] == mejor_compania, 'Company location'].iloc[0]
origen_cacao_mejor_compania = df.loc[df['Company'] == mejor_compania, 'Broad region of origin of bean'].iloc[0]
region_cacao_mejor_compania = df.loc[df['Company'] == mejor_compania, 'Specific region of origin of bean'].iloc[0]
st.write("La mejor compañía de acuerdo con la calificación promedio es:", mejor_compania, ", con un rating de:", calificacion_promedio_maxima)
st.write("La ubicación de la compañía:", ubicacion_mejor_compania)
st.write("El origen del cacao de la compañía:", origen_cacao_mejor_compania, ", específicamente de la región de:", region_cacao_mejor_compania)
st.subheader('Peor rating')
calificacion_promedio_por_compania = df.groupby('Company')['Rating'].mean()
peor_compania = calificacion_promedio_por_compania.idxmin()
calificacion_promedio_minima = calificacion_promedio_por_compania.min()
ubicacion_peor_compania = df.loc[df['Company'] == peor_compania, 'Company location'].iloc[0]
origen_cacao_peor_compania = df.loc[df['Company'] == peor_compania, 'Broad region of origin of bean'].iloc[0]
region_cacao_peor_compania = df.loc[df['Company'] == peor_compania, 'Specific region of origin of bean'].iloc[0]
st.write("La peor compañía de acuerdo con la calificación promedio es:", peor_compania, ", con un rating de:", calificacion_promedio_minima)
st.write("La ubicación de la compañía:", ubicacion_peor_compania)
st.write("El origen del cacao de la compañía:", origen_cacao_peor_compania, ", específicamente de la región de:", region_cacao_peor_compania)
print('\n')
chocolate_alto_cacao = df[df['Cocoa %'] > '60']
frecuencia_compania = chocolate_alto_cacao['Company'].value_counts()
compania_mas_comun = frecuencia_compania.idxmax()
st.write("La compañía que produce principalmente chocolate con más del 60% de cacao es:", compania_mas_comun)
st.bar_chart(frecuencia_compania, color='#D2691E')
st.caption('Con 47 chocolates arriba igual o arriba del porcentaje')
print('\n')
st.subheader('Año de revisión')
indice_ultima_revision = df['REF'].idxmax()
ref_ultima_revision = df.loc[indice_ultima_revision, 'REF']
fecha_ultima_revision = df.loc[indice_ultima_revision, 'Review date']
rating_ultima_revision = df.loc[indice_ultima_revision, 'Rating']
compania_ultima_revision = df.loc[indice_ultima_revision, 'Company']
st.write("La última revisión realizada tiene el REF:", ref_ultima_revision, ", hecha en el año:", fecha_ultima_revision)
st.write("Hecho hacia la compañía:", compania_ultima_revision, ", con un rating de:", rating_ultima_revision)
print('\n')
paises_latinoamerica = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'República Dominicana', 'Uruguay', 'Venezuela']
latinoamerica_df = df[df['Company location'].isin(paises_latinoamerica)]
num_companias_latinoamerica = latinoamerica_df.shape[0]
num_total_companias = df.shape[0]
porcentaje_latam = (num_companias_latinoamerica / num_total_companias) * 100
st.subheader('Porcentaje de compañías ubicadas en países de Latinoamérica')
st.write(f"Porcentaje de compañías ubicadas en países de Latinoamérica: {porcentaje_latam:.2f}%")
st.write('De 1795 valores de mi base de datos, 140 son el total de apariciones de empresas latam')
fig, ax = plt.subplots()
ax.bar(['Latinoamérica', 'Resto'], [porcentaje_latam, 100 - porcentaje_latam], color=['saddlebrown', 'peru'])
ax.set_ylabel('Porcentaje')
st.title('Porcentaje de compañías ubicadas en países de Latinoamérica')
st.write(fig)
print('\n')
st.title("Mapa")
st.write(" Este mapa muestra las diversas ubicaciones de las empresas de chocolate en diferentes países.")
iframe_html = """
<iframe src="https://www.google.com/maps/d/embed?mid=1GRxwVcOZs_qCF4DP6XLYb054iHCbdPI&ehbc=2E312F&noprof=1" width="640" height="480"></iframe>
"""
st.components.v1.html(iframe_html, width=700, height=500)









