### pip install qrcode Pillow
import qrcode
from PIL import Image

# QR instance
qr = qrcode.QRCode()

# QR data define
qr.add_data('https://everydayprogramming.dev/editor.html')

# data -> transfer into qr style
qr.make()

# make one
img = qr.make_image()

# save
img.save('qrcode1.jpg')
