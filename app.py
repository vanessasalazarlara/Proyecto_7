import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Información de vehículos en anuncios')
car_data = pd.read_csv('vehicles_us.csv') 
build_histogram = st.checkbox('Construir un histograma')
if build_histogram: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data,title='Distribución del kilometraje',x='odometer',color_discrete_sequence=["purple"])
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

build_scatter= st.checkbox('Construir gráfico de dispersion')
if build_scatter: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         
         # crear el gráfico
         fig=px.scatter(car_data, title="Relación entre kilometraje y precio" ,x="odometer", y="price",color_discrete_sequence=["purple"])
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)
         