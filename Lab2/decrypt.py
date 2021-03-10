import os
import sys
degree=1
text_mask = 0b11111111
img_mask = 0b11111111
text_mask <<= (8 - degree)
text_mask %= 256
img_mask >>= degree
img_mask <<= degree


 #extracting information from a picture
text = open("text.txt", 'w',encoding='utf-8')
encoded_bmp = open("steg.bmp", 'rb')
symbols_to_read=os.stat("Massage.txt").st_size
encoded_bmp.seek(54)
img_mask = ~img_mask

read = 0
while read < symbols_to_read:
    symbol = 0
    for bits_read in range(0, 8, degree):
        img_byte = int.from_bytes(encoded_bmp.read(1), sys.byteorder) & img_mask
        symbol <<= degree
        symbol |= img_byte
    read += 1
    text.write(chr(symbol))
    print (chr(symbol))

text.close()
encoded_bmp.close()