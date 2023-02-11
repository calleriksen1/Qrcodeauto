import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="testelucas"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('lucas.png')

#no prrmpt comando vai em "cd desktop", e em "python+nome da imagem"