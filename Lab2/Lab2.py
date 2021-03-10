import os
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

degree = 1


def ChBit():
    bin_oper = 0b11111111
    bin_add = 0b11111111
    bin_oper <<= (8 - degree)
    bin_oper %= 256
    bin_add >>= degree
    bin_add <<= degree
    return bin_oper, bin_add


##Embedding information in a picture
def coder(n):
    inp1 = Image.open("1.bmp")
    inp1_pix = np.array(inp1.getdata())
    inp1.close()
    text = open('text.txt', 'r')
    fileBMP = open('1.bmp', 'rb')
    stegoBMP = open('steg.bmp', 'wb')

    headBMP = fileBMP.read(54)
    stegoBMP.write(headBMP)
    bin_oper, bin_add = ChBit()
    for i in range(0, n):
        a = text.read(1)
        if not a:
            break
        a = ord(a)
        for i in range(0, 8, degree):
            img_byte = int.from_bytes(fileBMP.read(1), sys.byteorder) & bin_add
            bits = a & bin_oper
            bits >>= (8 - degree)
            img_byte |= bits
            stegoBMP.write(img_byte.to_bytes(1, sys.byteorder))
            a <<= degree
    stegoBMP.write(fileBMP.read())

    text.close()
    fileBMP.close()
    stegoBMP.close()
    inp = Image.open("steg.bmp")
    inp_pix = np.array(inp.getdata())
    return inp1_pix, inp_pix


    # extraction of information
def decoder():
    text = open("2.txt", 'w')
    encoded_bmp = open("steg.bmp", 'rb')
    symbols_to_read = os.stat("text.txt").st_size
    encoded_bmp.seek(54)
    bin_oper, bin_add = ChBit()
    bin_add = ~bin_add
    read = 0
    while read < symbols_to_read:
        symbol = 0
        for bits_read in range(0, 8, degree):
            img_byte = int.from_bytes(encoded_bmp.read(1), sys.byteorder) & bin_add
            symbol <<= degree
            symbol |= img_byte
        read += 1
        text.write(chr(symbol))
        print(chr(symbol))


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr
a=[1,5,10,20,30,40,50,100,500,1000]
b=[]
for i in a :
    inp1_pix, inp_pix = coder(11*i)
    b.append(PSNR(inp1_pix, inp_pix))
    print (b)

plt.figure(figsize=(15, 5))
plt.title('PSNR Graphic')
plt.plot(a, b)
plt.show()

