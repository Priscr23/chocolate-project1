import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
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
fig, ax = plt.subplots(figsize=(8, 6))
df['Bean type'].value_counts().plot(kind='bar', color='#A0522D', ax=ax)
st.subheader("Frecuencia de tipos de semilla")
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)
st.write("La moda de los tipos de frijoles es:", moda_bean)
print('\n')
st.subheader("Región de origen se semillas")
frecuencia_region = df['Broad region of origin of bean'].value_counts()
region_mas_comun = frecuencia_region.idxmax()
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title('Frecuencia de Región de Origen de los Frijoles de Cacao')
ax.set_xlabel('Región de Origen')
st.bar_chart(frecuencia_region, color='#D2691E')
st.write("La región de origen más común de las semillas de cacao es:", region_mas_comun)
print('\n')
st.subheader("Ubicación de compañía más común")
frecuencia_ubicacion = df['Company location'].value_counts()
ubicacion_mas_comun = frecuencia_ubicacion.idxmax()
st.bar_chart(frecuencia_ubicacion, color='#6B4423')
st.write("La ubicación más común de las compañías productoras de chocolate es:", ubicacion_mas_comun)
print('\n')
st.subheader("Porcentaje de cacao más preferible por las personas")
calificacion_promedio_porcentaje = df.groupby('Cocoa %')['Rating'].mean()
calificacion_promedio_porcentaje = calificacion_promedio_porcentaje.sort_values()
porcentaje_mas_popular = calificacion_promedio_porcentaje.idxmax()
st.bar_chart(calificacion_promedio_porcentaje, color='#8B4513')
st.write("El porcentaje de cacao más popular es:", porcentaje_mas_popular)
print('\n')
st.subheader("Cacao con mejor puntaje")
calificacion_promedio_por_tipo = df.groupby('Bean type')['Rating'].mean()
max_rating = calificacion_promedio_por_tipo.max()
tipos_mas_puntuados = calificacion_promedio_por_tipo[calificacion_promedio_por_tipo == max_rating].index.tolist()
st.bar_chart(calificacion_promedio_por_tipo, color='#DAA520')
st.write("Los tipos de semilla de frijol con los mayores puntajes son:")
for tipo in tipos_mas_puntuados:
    st.write(tipo)
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
st.subheader('Compañía que produce chocolate con +50%')
chocolate_alto_cacao = df[df['Cocoa %'] > '60']
frecuencia_compania = chocolate_alto_cacao['Company'].value_counts()
compania_mas_comun = frecuencia_compania.idxmax()
st.bar_chart(frecuencia_compania, color='#D2691E')
st.caption('Con 47 chocolates siendo igual o arriba del porcentaje')
st.write("La compañía que produce principalmente chocolate con más del 60% de cacao es:", compania_mas_comun)
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
st.subheader('Porcentaje de compañías ubicadas en países de Latinoamérica')
st.write(fig)
st.write("Representando un 7.8% latam.")
print('\n')
st.subheader('Cacao más frecuente/trabajado por localidad de las compañías')
produccion_por_pais_y_tipo = df.groupby(['Company location', 'Bean type']).size().reset_index(name='Frecuencia')
moda_por_pais = produccion_por_pais_y_tipo.groupby('Company location')['Bean type'].agg(lambda x: x.mode()[0])
st.write(moda_por_pais)
st.write('En la tabla se muestra el cacao más frecuente que se trabaja en cada compañía (ubicación donde se encuentra la empresa)')
print('\n')
st.subheader("Mapa")
iframe_html = """
<iframe src="https://www.google.com/maps/d/embed?mid=1GRxwVcOZs_qCF4DP6XLYb054iHCbdPI&ehbc=2E312F&noprof=1" width="640" height="480"></iframe>
"""
st.components.v1.html(iframe_html, width=700, height=500)
st.write(" Este mapa muestra las diversas ubicaciones de las empresas de chocolate en diferentes países.")
print('\n')
st.subheader('Clasificador')
df_c = pd.read_csv('C:/Users/prisc/apps/chocolate-project1/docs/datos_modificados1.csv')
df_c = pd.get_dummies(df_c, columns=['Company', 'Specific region of origin of bean', 'Company location', 'Broad region of origin of bean'])
df_c['Cocoa %'] = df_c['Cocoa %'].str.rstrip('%').astype(float)
X = df_c.drop('Bean type', axis=1)  
y = df_c['Bean type'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
train_score = knn.score(X_train_scaled, y_train)
test_score = knn.score(X_test_scaled, y_test)
st.write("Entrenamiento:", train_score)
st.write("Prueba:", test_score)
st.write("Precisión:", accuracy)
st.write('Con este clasificador nos ayuda a saber que tipo de semilla sería si en cierto caso la base tuviera datos faltantes, teniendo un puntaje considerado bueno para desglosar resultados.')
st.subheader('FACT ABOUT CACAO')
st.write('''El precio del cacao ha subido exponencialmente su precio en comparación del año pasado (2023) a este (2024),
        tanto así que a principios del mes de abril superó los $10,200 dólares.
         Esto se debe al cambio climático, a las grandes sequías en los países productores.
         Como consecuencia, los precios del chocolate comercial seguirán aumentando en los próximos dos años, como se ha hecho
         los útlimos años, donde el precio del chocolate ha aumentado el 11.6%, y debido a esto las empresas han comenzado a modificar 
         su producto agregando frutas o nueces para reducir el procentaje de chocolate y sustituir el cacao.
         Por otro lado, en plantaciones clandestinas de cacao, más en las zonas africanas, se dice que detrás de el cultivo de cacao,
         hay más de 1.5 millones de niños trabajando en las plantaciones, realizando trabajos y tareas peligrosas que ponen en riesgo
         su vida.
         ''')
st.image('C:/Users/prisc/apps/chocolate-project1/data/raw/3bfc39f13c899dce26c78914112d3305.jpg')
st.subheader('ACTIVIDAD')
st.write('Recuerden muy bien que color se están comiendo, y que sabor caracteriza a cada uno :)')
st.markdown(
    """
    <div style="width: 200px; height: 100px; background: linear-gradient(to right, green 50%, yellow 50%);"></div>
    """,
    unsafe_allow_html=True
)


















