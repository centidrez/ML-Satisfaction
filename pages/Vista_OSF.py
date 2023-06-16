from PIL import Image
import streamlit as st

# -- Remove Red line
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

with st.container():
    st.title("Análisis de Proyectos por OSF")
    st.write("""
    En este tablero, las OSF pueden acceder a 
    la retroalimentación proporcionada por los alumnos. 
    Pueden ver su ranking y desempeño en diferentes preguntas
    o aspectos evaluados. Además, esta visualización les permite 
    examinar los comentarios de los alumnos clasificados por 
    sentimiento, es decir, si son buenos, malos o regulares. 
    Esta funcionalidad brinda a las OSF una visión completa de 
    la percepción de los alumnos y les ayuda a identificar 
    áreas de mejora y fortalezas.
    """)
# -- Reporte PBI

with st.container():
    
    htmlpbi1 = '''
    <div style="justify-content: center; height: 100vh; width: 100vw;">
    <iframe title="RepTec" style="position: absolute; left: 50%; transform: translateX(-50%); height: 541.25px; width: 1140px; border: none;" src="https://app.powerbi.com/view?r=eyJrIjoiY2Y1MDA3MDgtMjQ2Mi00NDVkLThlMzctODYzNzNkOGMzNTRjIiwidCI6IjgwOWY3MzcxLTkwZjEtNDBkZC1iNGExLWZlMjM2MTA5ODJmYSIsImMiOjR9" allowFullScreen></iframe>
    </div>
    '''
    st.markdown(htmlpbi1, unsafe_allow_html=True)

st.sidebar.success("Vista por OSF")
