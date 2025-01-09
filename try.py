import qrcode

# Texto que quieres codificar en el QR
texto = "3507f4defe8ef3ff67b0988ac5542ca632ad189fc03ea896163102f78befdb1b99e0337217a0bf51211f0ae54493066ee0d6728ae01ade6f6031158ba9584c655a31ee8cbc47fc79a51f555bbca5fb55eb4e2a02de268c6bdc8f4e56cf3b03ed09239b06399fff3b584cc5622a16539956ac9d9bdb3270a895028dd939a2d7e4f0a7d03d3582a87a308a236d33443e61ac3d1b68da5fcc622a1653b1988ac56422dab30ff0d4a8279b341ccfe1a5dc1eda0aa801be0575b6ef5879cd3feaf0162ae21a3dd567da5fcc622a1653b1988ac5647805bf7266663b342b2fcfe84c46ede9dd5b856d10a1a1dba84bf2b120eac1b88ea00979e4d7b1988ac5542ca6f2ef11a3a3581e6f5896e50dc8363ee3fe5896657907c61d9f0bf058167cfc8c48fedfcb8f818ff7cf658c155896f7cb187fbf03e3eff77c5e78fcc8bade27007c2eede8c6ac28f8f7fc62b36031158ba9584c655ab1d735ffeb5afe8f87e7d2462e9ddaf8e54b701b9f8df648516f78cd7f128ba9584cc5622ad38a1de3fc1cd38f01fe8f87e7b6863ea0b450cad8dfdecd4d81fcca977378af233b3a78e43f83c5542ca662319569c5bec8ed69472352c07e6d5d9a6b37b71fd1451df8b7e9a43d205491409b71623fd9bd3abf81c5542ca662319569c596f1ff5ff3dfe063da5fcc622a1653b1988ac5542ca66231158ba9584cc5622a1653b1988ac5542ca66231158ba9584cc5622a1653b198caff017fea140b72140b420000000049454e44ae426082"

# Crear una instancia de la clase QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agregar datos al código QR
qr.add_data(texto)
qr.make(fit=True)

# Crear una imagen del código QR
img = qr.make_image(fill='black', back_color='white')

# Guardar la imagen en un archivo
img.save("bitsperdidos.png")
