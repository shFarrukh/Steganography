from PIL import Image
import numpy as np
import os
import sys


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr


inp2 = Image.open("steg.bmp")
inp2_pix = np.array(inp2.getdata())
inp = Image.open("1.bmp")
inp_pix = np.array(inp.getdata())
print(PSNR(inp_pix,inp2_pix))
