import os
import sys
degree=1
text_mask = 0b11111111
img_mask = 0b11111111
text_mask <<= (8 - degree)
text_mask %= 256
img_mask >>= degree
img_mask <<= degree

##Встраивание информации в картинку
##Embedding information in a picture
text = open('Massage.txt', 'r')
fileBMP = open('picture.bmp', 'rb')
stegoBMP = open('steg.bmp', 'wb')

headBMP = fileBMP.read(54)
stegoBMP.write(headBMP)

while True:
    a = text.read(1)
    if not a:
        break
    a = ord(a)
    for i in range(0, 8, degree):
        img_byte = int.from_bytes(fileBMP.read(1), sys.byteorder) & img_mask
        bits = a & text_mask
        bits >>= (8 - degree)
        img_byte |= bits
        stegoBMP.write(img_byte.to_bytes(1, sys.byteorder))
        a <<= degree
stegoBMP.write(fileBMP.read())

text.close()
fileBMP.close()
stegoBMP.close()


