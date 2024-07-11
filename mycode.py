import qrcode
img= qrcode.make("https://images.pexels.com/photos/158109/kodiak-brown-bear-adult-portrait-wildlife-158109.jpeg?cs=srgb&dl=pexels-pixabay-158109.jpg&fm=jpg")
img.save("mycode.png")
