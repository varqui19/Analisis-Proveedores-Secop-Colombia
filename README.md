# Pipeline de Datos y Dashboard de Proveedores del Estado (Colombia)📊 

Este proyecto implementa una solución completa de **Ingeniería y Analítica de Datos (End-to-End)**. Automatiza la extracción de más de 50,000 registros desde la API pública de Datos Abiertos de Colombia, realiza un proceso de limpieza y transformación (ETL) mediante Python, almacena la información de forma estructurada en SQL Server y finaliza con un tablero de control interactivo en Power BI enfocado en el análisis de mercado y auditoría operativa.

---

## Tecnologías Utilizadas

* **Extracción y ETL:** Python 3 (Pandas, Requests, SQLAlchemy, PyODBC)
* **Almacenamiento (Data Warehouse):** Microsoft SQL Server
* **Visualización & BI:** Power BI Desktop
* **Fuente de Datos:** API Socrata (Portal de Datos Abiertos Colombia)

---

## Arquitectura del Proyecto

El flujo de los datos sigue la siguiente estructura lógica:
1. **Extracción:** Consumo en vivo de la API del gobierno mitigando el límite por defecto de 1,000 filas mediante paginación dinámica (`$limit=50000`).
2. **Transformación (Python):** * Limpieza e higienización de encabezados.
   * Casteo estricto de tipos de datos para evitar la corrupción de identificadores numéricos (como los NITs y códigos que Pandas transformaba a flotantes `.0`).
   * Estandarización de cadenas de texto a mayúsculas fijas para corregir errores de digitación en municipios y nombres.
   * Formateo de fechas ISO a tipo Date estándar de SQL.
3. **Carga:** Inyección modular de datos en bloques (`chunksize=5000`) en SQL Server para optimizar el consumo de memoria RAM.
4. **Explotación:** Conexión directa desde Power BI para la creación de reportes analíticos de negocio.

---

## Consultas Estratégicas y Auditoría (SQL)

Dentro del motor se ejecutaron análisis avanzados para el negocio y el equipo de control interno:

* **Análisis de Densidad:** Identificación del Top 10 de municipios con mayor concentración de proveedores.
<img width="1431" height="803" alt="image" src="https://github.com/user-attachments/assets/aa3ef49d-88a1-4e7a-b7ba-8863046ad1c7" />

* **Auditoría de Formalidad:** Clasificación de correos electrónicos para determinar la madurez digital del mercado (Correos corporativos vs. dominios gratuitos como Gmail/Hotmail).
<img width="1431" height="803" alt="image" src="https://github.com/user-attachments/assets/aa3ef49d-88a1-4e7a-b7ba-8863046ad1c7" />

* **Alertas de Fraude (Empresas Fachada):** Detección de múltiples NITs diferentes que operan bajo un mismo número de teléfono registrado.
<img width="1431" height="803" alt="image" src="https://github.com/user-attachments/assets/aa3ef49d-88a1-4e7a-b7ba-8863046ad1c7" />
---

## Acceso al Proyecto

##  Visualización Interactiva
Puedes interactuar con el informe en tiempo real a través del siguiente enlace:

👉 **[Ver Dashboard Interactivo (Power BI Web)](https://app.powerbi.com/view?r=eyJrIjoiZDcyMWFlMDAtYWMwMC00NzUzLWFkNTMtNDQ0MjY4NDk4ZmQ0IiwidCI6IjgwMDc3YmJjLWJjNWEtNDc3NS04NzA4LTIwODkyNjVjMDAzMyIsImMiOjR9)**


## 📂 Repositorio de Archivos
* **Archivo del tablero:** [Descargar Dashboard Proveedores.pbix](./Dashboard_Proveedores_Estado_Colombia_Secop.pbix)
* **Script de automatización y ETL:** [etl_proveedores.py](./etl_secop.py)
* **Consultas de Auditoría:** [queries_auditoria.sql](./Querys.sql) 
* **Evidencias de Base de Datos:** [Capturas SQL Server](./images/)

*Nota: Este proyecto forma parte de mi portafolio profesional como Ingeniera de Sistemas.*

---

## Cómo Ejecutar el Proyecto

1. **Base de Datos:** Crear una base de datos vacía en SQL Server llamada `Datos_Colombia`.
2. **ETL:** Ejecutar el script `etl_secop.py` en Python para poblar la base de datos de manera automática desde la API.
3. **Dashboard:** Abrir el archivo `Dashboard_Proveedores_Estado_Colombia_Secop.pbix` en Power BI Desktop, el cual apunta localmente al servidor mediante el origen de datos configurado.