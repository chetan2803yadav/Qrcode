import qrcode 
from PIL import Image # MODUL IN PYTHON PIL

qr =qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=3,)

qr.add_data("https://www.youtube.com/shorts/9H9hEjYKzsk")
qr.make(fit=True)
Image=qr.make_image(fill_color="purple",black_color="white")

Image.save("Hanuman_shorts.png")