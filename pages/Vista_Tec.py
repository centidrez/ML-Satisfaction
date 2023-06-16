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
    st.title("Análisis de Proyectos Solidarios ")
    st.write("""
    Esta parte del prototipo se presenta como un tablero 
    interactivo que permite a los usuarios visualizar y evaluar
      el desempeño de las Organizaciones Socio Formadoras (OSF). 
      Mediante filtros, como el periodo, la categoría y la OSF específica, 
      los usuarios pueden explorar los rankings de las OSF y obtener una 
      visión detallada de su rendimiento. Esta visualización facilita 
      la comprensión de los datos y el seguimiento del progreso 
      de las organizaciones.
    """)
# -- Reporte PBI

with st.container():
    
    htmlpbi1 = '''
    <div style="justify-content: center; height: 100vh; width: 100vw;">
    <iframe title="RepTec" style="position: absolute; left: 50%; transform: translateX(-50%); height: 541.25px; width: 1140px; border: none;" src="https://app.powerbi.com/view?r=eyJrIjoiMDk2NjQ3YjQtNjViZi00ZTYzLWE0MjMtMDA1MTMyMDc2Nzc0IiwidCI6IjgwOWY3MzcxLTkwZjEtNDBkZC1iNGExLWZlMjM2MTA5ODJmYSIsImMiOjR9&pageName=ReportSection30d3f5672501d60b5d7a" allowFullScreen></iframe>
    </div>
    '''
    st.markdown(htmlpbi1, unsafe_allow_html=True)

st.sidebar.success("Vista de Servicio Social")