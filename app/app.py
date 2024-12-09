from pymongo import MongoClient
from dotenv import load_dotenv
import os
import plotly.express as px
import pandas as pd


# Cargar variables de entorno
load_dotenv()

# Conexión a MongoDB
uri = os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client["Madrid"]
collection = db["peatones"]

# Probar conexión
try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB!")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")

# Consulta para obtener datos
datos = list(collection.find())
print(datos)

