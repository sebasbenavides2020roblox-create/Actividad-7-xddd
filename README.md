# Actividad 7 — Bases de datos, Python y MySQL

Repositorio correspondiente a la **Actividad 7**.

## PRIMER PUNTO

### 1. Tipos de datos
Los tipos de datos más comunes son:

| Tipo | Uso | Ejemplo |
|---|---|---|
| INT | Números enteros | Edad: 17 |
| VARCHAR | Texto corto | Nombre: "Sebastián" |
| DATE | Fechas | 2026-09-30 |
| DECIMAL | Números decimales precisos | Precio: 12500.50 |
| BOOLEAN | Verdadero o falso | Disponible: TRUE |
| TEXT | Texto largo | Descripción de un producto |

### 2. Ejemplos
- **INT:** edad, cantidad de productos, número de registro.
- **VARCHAR:** nombre, marca, correo, dirección.
- **DATE:** fecha de nacimiento, fecha de compra, fecha de una cita.
- **DECIMAL:** precio de un producto o salario.
- **BOOLEAN:** si un producto está disponible.
- **TEXT:** descripción u observaciones.

### 3. ¿Qué pasaría si no existieran los sistemas informáticos?
La información tendría que manejarse principalmente de forma manual. Esto aumentaría el tiempo de los procesos y la posibilidad de cometer errores. También sería más difícil buscar, actualizar, compartir y proteger grandes cantidades de datos.

### 4. Impacto en sectores
**Banca:** las transacciones y consultas serían más lentas y dependerían de registros físicos.

**Salud:** sería más difícil consultar historias clínicas, citas y resultados.

**Comercio:** controlar inventarios, ventas y clientes requeriría más trabajo manual.

Ejemplos históricos:
1. Registros bancarios en libros y documentos físicos.
2. Historias clínicas almacenadas en carpetas de papel.
3. Inventarios comerciales registrados manualmente.

### 5. Antes de las computadoras
Las transacciones bancarias se hacían presencialmente y se registraban en formularios y libros. Las solicitudes médicas y las citas también se gestionaban principalmente mediante documentos físicos, llamadas o atención presencial.

### 6. Comparación

| Proceso | Antes | Con sistemas informáticos |
|---|---|---|
| Banco | Registros físicos y atención presencial | Sistemas digitales y consultas rápidas |
| Citas médicas | Formularios, llamadas y agendas físicas | Sistemas de citas |
| Historias clínicas | Carpetas de papel | Bases de datos |
| Inventarios | Conteo y registro manual | Control digital |

### 7. Tabla Automóvil
Modelo,Marca
2025,BMW
2024,Toyota
2026,Chevrolet

### 8. Tabla Paciente
Atributos: **Nombre, Edad**.

### 9. Tabla Producto
Atributos: **Nombre, Precio**.

### 10. Registros
Se ingresaron al menos tres registros por cada tabla. Los datos están en la carpeta `datos/`.

### 11. Operaciones realizadas
En `python/operaciones.py` se muestran ejemplos de:
- Filtrar datos.
- Ordenar datos.
- Modificar registros.
- Eliminar registros.

### 12. Excel frente a una base de datos real
Excel es útil para organizar cantidades pequeñas o medianas de información y realizar cálculos de manera sencilla. Una base de datos está diseñada específicamente para manejar grandes cantidades de datos, relacionar diferentes tablas, controlar usuarios y realizar consultas de forma más estructurada.

### 13. Evidencia
Los archivos y commits de este repositorio sirven como evidencia del desarrollo de la actividad.

---

# SEGUNDO PUNTO — Python y Zen

## 1. Filosofía de Python
La filosofía de Python busca que el código sea sencillo, claro y fácil de leer. Una de las ideas que más me gusta es que la legibilidad cuenta, porque un código que se entiende fácilmente también es más sencillo de mantener y corregir.

## 2. Desarrollo en Python
El archivo `python/zen_python.py` desarrolla el punto anterior con ejemplos.

## 3. Librerías
El archivo `python/librerias.py` explica:
- **pandas:** análisis y organización de datos mediante DataFrames.
- **polars:** procesamiento eficiente de datos.
- **SciPy:** herramientas para matemáticas, ciencia e ingeniería.
- **MySQL:** conexión entre Python y una base de datos mediante un conector.

## 4. Infografía
La infografía sobre MySQL con Python y sus aplicaciones está en `infografia.html`.

---

# TERCER PUNTO — Propuesta de aplicación

## Sistema de gestión de productos y ventas

La aplicación permitirá administrar productos, usuarios y ventas mediante una base de datos.

### Tablas
**Producto:** id, nombre, precio, categoría, stock, fecha_registro.

**Categoría:** id, nombre.

**Usuario:** id, nombre, correo.

**Venta:** id, usuario_id, fecha, total.

**DetalleVenta:** id, venta_id, producto_id, cantidad, precio.

### Funciones
- Registrar, editar y eliminar productos.
- Buscar y filtrar productos.
- Ordenar por precio o stock.
- Registrar ventas.
- Consultar clientes.
- Generar reportes.

### Requisitos funcionales
1. Registrar productos.
2. Modificar y eliminar productos.
3. Consultar y filtrar información.
4. Registrar ventas.
5. Relacionar ventas con productos.
6. Generar reportes.

### Requisitos no funcionales
1. Interfaz fácil de utilizar.
2. Datos organizados.
3. Control de acceso.
4. Respuesta rápida.
5. Copias de seguridad.
6. Adaptación a diferentes dispositivos.

## Estructura

```
Actividad-7-xddd/
├── README.md
├── datos/
│   ├── automovil.csv
│   ├── paciente.csv
│   └── producto.csv
├── python/
│   ├── zen_python.py
│   ├── operaciones.py
│   └── librerias.py
├── documentacion/
│   ├── tipos_de_datos.md
│   ├── antes_de_las_computadoras.md
│   └── propuesta_aplicacion.md
└── infografia.html
```
