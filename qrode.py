import qrcode as qr
img= qr.make("https://www.youtube.com/channel/UC3qrp6cJCXk-TYzDhRz-WEA")
img.save("storyscoop_youtube.png")