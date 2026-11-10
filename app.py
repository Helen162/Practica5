import streamlit as st
from modulos.login import login
from modulos.VENTAS import mostrar_venta
from modulos.EMPLEADOS import mostrar_empleados

# Inicializar variables de sesión
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False
if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

# Comprobar si el usuario inició sesión
if st.session_state["sesion_iniciada"]:
    st.sidebar.title("Menú de Navegación")
    st.sidebar.write(f"Usuario: {st.session_state['usuario']}")
    
    opciones = [
        "Ventas",
        "Empleados",
        "Información"
    ]
    
    seleccion = st.sidebar.selectbox(
        "Seleccione una opción",
        opciones
    )
    
    # Mostrar módulo de ventas
    if seleccion == "Ventas":
        mostrar_venta()
        
    # Mostrar módulo de empleados
    elif seleccion == "Empleados":
        mostrar_empleados()
        
    # Mostrar módulo de información
    elif seleccion == "Información":
        st.header("Información del sistema")
        st.write(
            "Aplicación desarrollada para la Práctica #6 "
            "con gestión de usuarios, ventas y empleados."
        )
        
    # Cerrar sesión
    if st.sidebar.button("Cerrar sesión"):
        st.session_state["sesion_iniciada"] = False
        st.session_state["usuario"] = ""
        st.rerun()
else:
    # Si no hay sesión iniciada, mostrar login
    login()
