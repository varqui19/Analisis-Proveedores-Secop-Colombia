import pandas as pd
import requests
import urllib
from sqlalchemy import create_engine
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. URL de la API
url_api = "https://datos.gov.co/resource/qmzu-gj57.json?$limit=50000"

print("Conectando con la API de Datos Abiertos Colombia...")
response = requests.get(url_api, verify=False)
datos_json = response.json()

# Convertimos la respuesta en una tabla de Pandas
df = pd.DataFrame(datos_json)

# Limpiamos los encabezados (minúsculas y sin espacios)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

print("Datos cargados. Iniciando limpieza de columnas...")

# ==========================================
# PROCESO DE LIMPIEZA (ETL)
# ==========================================

# 1. Forzar a que los Códigos y NIT sean TEXTO limpio
columnas_codigo = ['codigo', 'nit', 'numero_doc_representante_legal', 'telefono', 'telefono_representante_legal']
for col in columnas_codigo:
    if col in df.columns:
        # Reemplazamos los nulos por texto vacío y quitamos cualquier decimal '.0'
        df[col] = df[col].astype(str).str.replace(r'\.0$', '', regex=True).str.strip()

# 2. Formatear la Fecha de Creación para que SQL la entienda de verdad
if 'fecha_creaci_n' in df.columns:
    df['fecha_creaci_n'] = pd.to_datetime(df['fecha_creaci_n'], errors='coerce').dt.strftime('%Y-%m-%d')
elif 'fecha_creacion' in df.columns:
    df['fecha_creacion'] = pd.to_datetime(df['fecha_creacion'], errors='coerce').dt.strftime('%Y-%m-%d')

# 3. Estandarizar textos desordenados (Todo a MAYÚSCULAS fijas y sin espacios)
columnas_texto = ['nombre', 'municipio', 'departamento', 'tipo_empresa', 'nombre_representante_legal']
for col in columnas_texto:
    if col in df.columns:
        df[col] = df[col].astype(str).str.upper().str.strip()

print(f"¡Conexión exitosa con la data del gobierno! Descargadas {len(df)} filas reales en memoria.")

# ==========================================
# 2. CONFIGURACIÓN DE CONEXIÓN A SQL SERVER
# ==========================================
nombre_servidor = "."  
nombre_base_datos = "Datos_Colombia" 

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={nombre_servidor};"
    f"DATABASE={nombre_base_datos};"
    f"Trusted_Connection=yes;"
)

conexion_string = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(conexion_string)

print(f"Inyectando las filas en la tabla 'secop_colombia'...")

# Subimos los datos en bloques cómodos de 5,000 en 5,000 para cuidar el procesador
df.to_sql('secop_colombia', con=engine, if_exists='replace', index=False, chunksize=5000)

print("¡CONEXION Y CARGA DE DATOS TERMINADA!")

