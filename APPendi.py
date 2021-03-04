import sqlite3
import streamlit as st

st.title("Bienvenido")
st.image("https://github.com/mdfnunez/APPendi/blob/main/APPendi.jpg")
c=sqlite3.connect("Omega.db")
con=c.cursor()
creartabla=c.execute("""CREATE TABLE IF NOT EXISTS Theta(
Nombre TEXT,
Edad INTEGER,
PeliculaFavorita TEXT)""")
c.commit()
st.cache()
Nombre=st.text_input("Nombre: ")
Edad=st.number_input("Edad: ")
Pelifav=st.text_input("Pelicula favorita")
Aplicar=st.button("Salvar cambios")
if Aplicar==True:
    c.execute("INSERT INTO Theta(Nombre,Edad,Peliculafavorita)VALUES (?,?,?)""", (Nombre, Edad, Pelifav))
    c.commit()
    c.close()


