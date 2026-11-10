import mysql.connector
import streamlit as st


def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="TU_HOST",
            user="TU_USUARIO",
            password="TU_CONTRASENA",
            database="TU_BASE_DE_DATOS",
            port=3306
        )
        return conexion
    except Exception as error:
        st.error(f"Error de conexión: {error}")
        return None
