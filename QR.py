import os
import uuid
import qrcode
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("localhost", 27017)
db = client["QR"]
collection = db["id_productos"]

# Crear una función para generar el código QR y guardarlo
def generar_qr(contenido, filename):
    if not os.path.exists(filename):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(contenido)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
        print(f"QR guardado como {filename}")
    else:
        print(f"El QR ya existe como {filename}")



# Crear una función para insertar datos en Mongodb(forma local)
def insertar_en_mongo(id_producto, filename):
    documento = {
        "id_producto": id_producto,
        "qr_filename": filename,
    }
    collection.insert_one(documento)
    print("Documento insertado en la base de datos")


# Generar un código QR con ID único(id random)
id_producto = str(uuid.uuid4())

qr_filename = f"qr_{id_producto}.png"

contenido_qr = f"ID del producto: {id_producto}"  # Personaliza el QR(el que vemos )

generar_qr(contenido_qr, qr_filename)

insertar_en_mongo(id_producto, qr_filename)