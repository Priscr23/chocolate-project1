import streamlit as st
import pandas as pd
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

df=pd.read_csv('C:/Users/prisc/apps/chocolate-project1/reports/streamlit/data_limpia.csv')
st.dataframe(df)
print('\n')