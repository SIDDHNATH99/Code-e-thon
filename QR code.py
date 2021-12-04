import qrcode

img = qrcode.make("https://www.facebook.com/")
img.save("facebook.jpg")