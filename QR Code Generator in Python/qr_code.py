import qrcode # type: ignore

# URL to encode in the QR Code
url = "https://youtu.be/aVQJGr2J8io?si=FTOMEvQLPBD8x3kx"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Control the size of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4  # Border thickness (default is 4)
)


# Add url to QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image
img.save("qrcode.png")

# Display the QR code (optional)
img.show()