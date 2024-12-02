from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener la URI desde el archivo .env
uri = os.getenv("MONGO_URI")

# Crear un cliente
client = MongoClient(uri)

# Probar conexión
try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB!")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")
