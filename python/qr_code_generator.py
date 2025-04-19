import qrcode

data = input("Enter the text or URL: ").strip()
file_name = input("Enter the file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)
print(f"QR code saved as {file_name}")
