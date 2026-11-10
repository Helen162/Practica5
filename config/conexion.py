import mysql.connector
import streamlit as st


def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="by8sol7gd9p6ir6zueut-mysql.services.clever-cloud.com",
            user="u8jd65h12y411u2v",
            password="4KvhQa1h6Fk5wt4NL8v1",
            database="by8sol7gd9p6ir6zueut",
            port=3306
        )
        return conexion
    except Exception as error:
        st.error(f"Error de conexión: {error}")
        return None
