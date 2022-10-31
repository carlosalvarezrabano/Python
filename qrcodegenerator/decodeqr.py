#Programa para decodificar el código qr generado con qrcodegenerator.py

#Importante instalar estos módulos para que funcione el programa
from pyzbar.pyzbar import decode
from PIL import Image

#Apuntar a ruta donde se encuentra el código qr ya generado
img = Image.open('<rutadedestino>/myqrcode.png')

result = decode(img)

#Línea opcional para comprobar que todo el proceso se ha realizado correctamente
print(result)