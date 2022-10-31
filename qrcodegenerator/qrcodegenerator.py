#Necesario importar este módulo para que el programa funcione
import qrcode

data = 'Patata'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)
qr.make(fit=True)

#Customizar el color del código qr y el fondo (se puede cambiar a gusto del consumidor)
img = qr.make_image(fill_color = 'red', back_color = 'white')

#Editar para apuntar a una ruta de destino donde encontrar el código generado
img.save('<ruta de destino>/myqrcode.png')