### pip install qrcode Pillow
import qrcode
from PIL import Image

# QRコードのインスタンスを作る
qr = qrcode.QRCode()

# QRコードにするデータ、URLなどの指定
qr.add_data('https://everydayprogramming.dev/editor.html')

# data -> transfer into qr style
qr.make()

# make one
img = qr.make_image()

# save
img.save('qrcode1.jpg')
