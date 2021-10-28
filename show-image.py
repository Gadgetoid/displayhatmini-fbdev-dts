#!/usr/bin/env python3
import os
import sys
import numpy as np

from PIL import Image

def image_to_bytes(image):
    pb = np.array(image.convert('RGB')).astype('uint16')

    # Mask and shift the 888 RGB into 565 RGB
    red   = (pb[..., [0]] & 0xf8) << 8
    green = (pb[..., [1]] & 0xfc) << 3
    blue  = (pb[..., [2]] & 0xf8) >> 3

    # Stick 'em together
    result = red | green | blue

    # Output the raw bytes
    return result.tobytes()

try:
    filename = sys.argv[1]
except IndexError:
    filename = "bilgetank-test-card.png"

image = Image.open(filename)

print("Resizing image to 320x240")
image = image.resize((320, 240))
image.save("bilgetank-test-card-1.png")

fbdev = os.getenv('FRAMEBUFFER', '/dev/fb1')
print(f"Displaying to {fbdev}")
with open(fbdev, 'wb') as fb:
    fb.write(image_to_bytes(image))


