#APPendi: para la comparacion del registro electronico vs juicio clinico en el diagnostico correcto de apendicitis aguda
import streamlit as st
from PIL import Image
st.image("https://github.com/mdfnunez/APPendi/blob/main/APPendi.jpg?raw=true")
st.subheader("Protocolo de estudio de pacientes con apendicitis aguda, IMSS")
st.write("")
st.subheader("Registro de nuevo paciente")
Nombre=st.text_input("Nombre")
Edad=st.number_input("Edad")
fechanac=st.date_input("Fecha de nacimiento")
Nss=st.number_input("Numero de seguridad social")
Genero=st.text_input("Genero")
st.image("https://github.com/mdfnunez/APPendi/blob/main/Especialidades.jpg?raw=true")
