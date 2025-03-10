#libraries
import qrcode
import numpy as np
from PIL import Image
import os

#os
base_dir = os.path.dirname(os.path.abspath(__file__))
path_image = os.path.join(base_dir, 'derstenatildik.jpg')

#image
image = Image.open(path_image)
gray_image = image.convert('L')
width, height = image.size

#numpy
np.set_printoptions(threshold=np.inf)
rgb_values = np.array(gray_image)
print(rgb_values.shape)

#qr
qr = qrcode.QRCode(
        version=10, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4)
qr.add_data(rgb_values)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
file_path = os.path.join("derstenatildik2.png")

img.save(file_path)





