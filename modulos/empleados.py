import streamlit as st
from config.conexion import obtener_conexion


def mostrar_empleado():
    st.header("Registrar empleado")

    with st.form("form_empleado"):
        nombre = st.text_input(
            "Nombre del empleado"
        )

        cargo = st.text_input(
            "Cargo"
        )

        fecha_ingreso = st.date_input(
            "Fecha de ingreso"
        )

        guardar = st.form_submit_button(
            "Guardar empleado"
        )

    if guardar:
        if nombre.strip() == "" or cargo.strip() == "":
            st.warning(
                "Debe ingresar el nombre y el cargo."
            )
        else:
            conexion = None
            cursor = None

            try:
                conexion = obtener_conexion()

                if conexion is None:
                    return

                cursor = conexion.cursor()

                consulta = """
                INSERT INTO EMPLEADOS
                (Nombre, Cargo, Fecha_Ingreso)
                VALUES (%s, %s, %s)
                """

                cursor.execute(
                    consulta,
                    (nombre, cargo, fecha_ingreso)
                )

                conexion.commit()

                st.success(
                    "Empleado registrado correctamente."
                )

            except Exception as error:
                if conexion is not None:
                    conexion.rollback()

                st.error(
                    f"Error al registrar el empleado: {error}"
                )

            finally:
                if cursor is not None:
                    cursor.close()

                if (
                    conexion is not None
                    and conexion.is_connected()
                ):
                    conexion.close()
