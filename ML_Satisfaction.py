from PIL import Image
import streamlit as st
import pandas as pd
import tensorflow


st.set_page_config(page_title="ML Satisfaction",layout="wide")

# -- Importar imágenes
img_impacto = Image.open("images/ps.jpg")

# -- Remove Red line
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# -- Header(Titulo y objetivos)
with st.container():
    st.title("Analisis de Satisfacción sobre encuestas de Proyectos Solidarios")
    st.write("##")
    st.subheader("Problemática")
    st.write("""La Dirección de Servicio Social del campus Monterrey busca predecir 
    con precisión el grado de satisfacción de estudiantes en su experiencia con la Organización
    Socio Formadora (OSF). Para ello, se tomarán datos recopilados de encuestas de satisfacción 
    en las que los estudiantes han calificado a sus OSF.""")
    st.subheader("Objetivo general")
    st.write("""
    - Predecir con precisión el grado de satisfacción de los estudiantes en su 
    experiencia con una Organización Socio Formadora.
    """)
    st.subheader("Objetivos específicos")
    st.write("""
    - Realizar un análisis descriptivo para identificar las variables mayormente predictoras de 
    un alto nivel de satisfacción con la OSF.
    - Identificar diversos insights a partir de los datos.
    - Desarrollar un algoritmo que asigne un valor numérico representativo del nivel de satisfacción de los 
    estudiantes encuestados con cada una de las OSF, considerando todas las preguntas de la encuesta.
    - Realizar un análisis predictivo, mediante un modelo de clasificación capaz de predecir con 
    precisión el nivel de satisfacción de los estudiantes con la OSF.
    - Analizar textos con herramientas de NLP.
    """)
# -- Impacto proyecto
with st.container():
    st.write("---")
    left_column, right_column = st.columns((0.60,0.40), gap="large")
    with left_column:
        st.header("Impacto del Proyecto")
        st.write("""
        Debido a la gran cantidad de causas que se apoyan mediante los proyectos 
        solidarios del Tecnológico de Monterrey. Consideramos que este modelo tiene 
        como principal impacto el fortalecimiento de las comunidades. Esto se debe a 
        que los proyectos solidarios que maneja la OSF abordan diversas problemáticas 
        sociales, como la educación, el acceso a servicios básicos, el emprendimiento, 
        la inclusión y la sostenibilidad ambiental.
        Mediante nuestro proyecto buscamos mejorar la experiencia de los estudiantes 
        que se enlistan con la OSF, generando una mayor visibilidad a los proyectos con mejores reseñas, 
        reportando las malas experiencias de los estudiantes y brindando transparencia y confianza sobre 
        los proyectos con los que se trabaja.
        """)
    with right_column:
        st.write("##")
        st.image(img_impacto,width=400)

# -- Barra Lateral
st.sidebar.success("Seleccione una de las Vistas por Usuario")


