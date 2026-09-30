import pandas as pd

automovil = pd.read_csv("../datos/automovil.csv")
paciente = pd.read_csv("../datos/paciente.csv")
producto = pd.read_csv("../datos/producto.csv")

# 1. Filtrar
productos_caros = producto[producto["Precio"] > 150000]
print("Productos con precio mayor a $150.000:")
print(productos_caros)

# 2. Ordenar
productos_ordenados = producto.sort_values(by="Precio", ascending=False)
print("\nProductos de mayor a menor precio:")
print(productos_ordenados)

# 3. Modificar
producto.loc[producto["Nombre"] == "Teclado", "Precio"] = 130000
print("\nProducto modificado:")
print(producto)

# 4. Eliminar
producto = producto[producto["Nombre"] != "Audífonos"]
print("\nDespués de eliminar Audífonos:")
print(producto)
