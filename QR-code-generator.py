import qrcode

data = input("Enter text or URL to encode: ")
qr = qrcode.make(data)

qr.save("qrcode.png")
print("QR code generated and saved as 'qrcode.png'.")