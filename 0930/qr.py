import qrcode
import PIL

qr = qrcode.QRCode()
qr.add_data('https://app.notion.com/p/Day5-3a556652fded8090a040e2865659163b')
qr.make()

img = qr.make_image()
img.save("qrcode.png")

print("Done")
