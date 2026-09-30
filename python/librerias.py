# Librerías de Python y conexión con MySQL

# pandas: análisis y organización de datos
import pandas as pd
datos = pd.DataFrame({
    "producto": ["Portátil", "Teclado"],
    "precio": [2500000, 120000]
})
print(datos)

# polars: procesamiento eficiente de datos
import polars as pl
datos_polars = pl.DataFrame({
    "producto": ["Portátil", "Teclado"],
    "precio": [2500000, 120000]
})
print(datos_polars)

# SciPy: matemáticas, ciencia y estadística
from scipy import stats

# MySQL: conexión desde Python
# Instalar con: pip install mysql-connector-python
import mysql.connector

# Ejemplo de conexión. No usar contraseñas reales en el repositorio.
# conexion = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="tu_password",
#     database="actividad7"
# )
# cursor = conexion.cursor()
# cursor.execute("SELECT * FROM producto")
# for fila in cursor.fetchall():
#     print(fila)
# cursor.close()
# conexion.close()
