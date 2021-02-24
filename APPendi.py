#ApendiAPP: para la comparacion del registro electronico vs juicio clinico en el diagnostico correcto de apendicitis aguda

import streamlit as st
from PIL import Image

st.image("https://github.com/mdfnunez/APPendi/blob/main/APPendi.jpg")
st.title("Centro Medico Hola amor Siglo XXI")
st.subheader("Protocolo de estudio de pacientes con apendicitis aguda, IMSS")
#Escribir palabras simples sin formato
#poner un boton
#st.button("A")
#Barra lateral, se puede colocar checkbox, texto, slider, etc.


#BARRA LATERAL
st.subheader("Panel de busqueda y registro")
buscarpaciente = st.button("Busqueda de paciente")
if buscarpaciente:
    filename=st.text_input("Ingresa numero de seguridad social (NSS)")
    try:
        with open(filename+".txt") as input:
            st.text(input.read())
    except:
        st.write("Paciente no encontrado")
Botonregistro=st.button("Nuevo registro")
if Botonregistro:
    st.write("")
    st.subheader("Favor de contestar las siguientes preguntas sin ayuda de nadie")

    Nombreregistro=st.text_input("Nombre completo")
    Edadregistro=st.date_input("Fecha de nacimiento")
    genero=st.multiselect("Cual es su genero",["Hombre","Mujer"])
    st.write("")
    if genero == "Hombre":
        EVA = st.slider("Cuanto dolor tiene en este momento",0,10)
        dolorFID=st.checkbox("Ha tenido dolor en el ombligo que migra o avanza a la parte baja y derecha de su abdomen en las ultimas 24 hrs")
        fiebre=st.checkbox("Ha tenido fiebre")
        anorexia=st.checkbox("Ha tenido falta de apetito en las ultimas 24 hrs")
        vomito=st.checkbox("Ha vomitado o presentado nausea en las ultimas 24 hrs")
        flujo=st.checkbox("Ha tenido flujo vaginal, comezon o dolor con las relaciones sexuales")
    elif genero == "Mujer":
        EVA = st.slider("Cuanto dolor tiene en este momento", 0, 10)
        dolorFID = st.checkbox("Ha tenido dolor en el ombligo que migra o avanza a la parte baja y derecha de su abdomen en las ultimas 24 hrs")
        fiebre = st.checkbox("Ha tenido fiebre")
        anorexia = st.checkbox("Ha tenido falta de apetito en las ultimas 24 hrs")
        vomito = st.checkbox("Ha vomitado o presentado nausea en las ultimas 24 hrs")

