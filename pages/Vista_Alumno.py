from PIL import Image
import streamlit as st
import pandas as pd
import tensorflow as tf
import pickle
from tensorflow.keras.models import Sequential, model_from_yaml
from tensorflow.keras.layers import Dense

# -- Data
df_coment=pd.read_csv("https://raw.githubusercontent.com/EstebanPerez25/ACD-Modelo_predictivo_de_satisfacion/main/DataBase.csv")
osf_valores = df_coment['osf'].unique().tolist()

# -- Leer modelo
#lin_model = pd.read_pickle(r'm_dnn.pkl')
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

layer = tf.keras.layers.Dense(2, name="dense")
model = tf.keras.Sequential([layer], name="model")
print(model.built)
with tf.name_scope("parent"):
    with tf.name_scope(model.name):
        model.build((None, 3))
print([v.name for v in model.variables])
#lin_model = pickle.load(open('m_dnn.pkl', 'rb'), encoding='latin1')
lin_model = pd.read_pickle(r'm_dnn.pkl', compression='infer')

# -- Función modelo
def prediction(lstat, rm):
    if lstat != None and lstat != '' and rm != None and rm != '':
        try:
            precio = lin_model.predict([[float(lstat), float(rm)]])
            return str(round(float(precio[0]), 4))
        except ValueError:
            return 'Value error in lstat or rm'

# -- Remove Red line
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

def main():
    # -- Descripción de la vista
    with st.container():
        st.title("Predicción de Satisfacción por Alumno")
        st.write("""Nuestro modelo utiliza una red neuronal 
        entrenada para predecir el nivel de satisfacción por
        Organización Socio Formadora a lo largo del tiempo.
        Para lograr esto, hemos alimentado la red neuronal
        con datos de proyectos presentes en 3 periodos académicos.
        Si desea obtener una predicción, simplemente seleccione 
        la Organización Socio Formadora y el periodo en el cual 
        desea evaluarla. De esta manera, podrá obtener una 
        evaluación del proyecto que desee consultar en una 
        escala del 1 al 5.""")

    # -- Parámetros
    asignaciones = {'INV22': 1, 'FJ22': 2, 'AD22': 3, 'INV23': 4, 'FJ23': 5, 'AD23': 6, 'INV23': 7}
    asignaciones2 = {osf: i+1 for i, osf in enumerate(osf_valores)}
    # -- Inputs
    with st.container():
        periodo = st.selectbox(
        'Seleccione el periodo a predecir:',
        ('INV22', 'FJ22', 'AD22', 'INV23', 'FJ23', 'AD23', 'INV23'))
        osf = st.selectbox(
        'Ingrese la OSF a predecir:',
        (osf_valores))
        pred_button = st.button('Predecir')

    lstat = asignaciones.get(periodo)
    rm= asignaciones2.get(osf)

    # -- Predicción
    if pred_button:
        pred = prediction(lstat, rm)
        st.write("El promedio de evaluación para la OSF {} en el Periodo {} es: {}".format(osf, periodo, pred))

    st.sidebar.success("Predicción para Alumno")

if __name__ == "__main__":
    main()