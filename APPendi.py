import sqlite3
import streamlit as st

st.sidebar.image("https://github.com/mdfnunez/APPendi/blob/main/CMNXXI.jpg",None,300,350)
st.sidebar.title("Centro Medico Nacional Siglo XXI")
st.sidebar.subheader("Hospital de especialidades")

#Agregar logo de la app
#Agregar logo para cada seleccion en el sidebar
#crear tabla y agregar columnas
db=sqlite3.connect("Alpha.db")
c=db.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS pac(
NSS INT PRIMARY KEY NOT NULL,
Nombre TEXT NOT NULL
)""")
db.commit()
NSS=st.number_input("NSS: ",1,None,1,1)
Nombre=st.text_input("Nombre: ")
Registrar=st.button("Registrar")
if Registrar == True:
    c.execute('INSERT INTO pac VALUES(?,?)',(NSS,Nombre))
    db.commit()
    db.close()
    st.text("Se agregaron los datos")

#Ver datos imprime los datos despues de presionar el boton
verdatos=st.button("Ver registro")
if verdatos==True:
    VER=c.execute("SELECT * FROM pac")

    rows = c.fetchall()

    for row in rows:
        st.text(row)
#Sidebar
st.sidebar.selectbox("Selecciona",("Registro de paciente","Nota de ingreso","Nota de evolucion","Indicaciones"))
