import sqlite3
import streamlit as st

st.title("Bienvenido")
st.image("APPendi.jpg")
c=sqlite3.connect("Omega.db")
con=c.cursor()
creartabla=c.execute("""CREATE TABLE IF NOT EXISTS DATABASE_URL(
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
    c.execute("INSERT INTO theta(Nombre,Edad,Peliculafavorita)VALUES (?,?,?)""", (Nombre, Edad, Pelifav))
    c.commit()
    c.close()


