import sqlite3
import pandas
import streamlit as st
st.write("Bienvenidos")
print("Bienvenido, iniciemos "
      ""
      ""
      "")

print("Registra tus datos")
c=sqlite3.connect("Alpha.db")
con=c.cursor()


def nuevatabla():
      c
      c.execute(""" CREATE TABLE IF NOT EXISTS pa (
      NSS INTEGER PRIMARY KEY UNIQUE,
      Nombre TEXT,
      Edad INTEGER
      )""")
      c.commit()
      c.close()

#### agregar datos a la base de datos
try:
      NSS=int(st.input_text("Numero de seguridad social: "))
      Nombre=st.input_text("Nombre del paciente: ")
      Edad=int(st.input_text("Edad del paciente"))

      c.execute("INSERT INTO pa(NSS,Nombre,Edad)VALUES (?,?,?)""", (NSS,Nombre,Edad))

      c.commit()
      print("Registro existoso")
except :
       print("Existe un registro previo con ese numero de seguridad social")

def get_posts():
    c.execute("SELECT * FROM pa")
    print(con.fetchall())

get_posts()

c.close()

