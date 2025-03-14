#libraries
import qrcode
import numpy as np
from PIL import Image
import os
import zlib
import base64


#os
base_dir = os.path.dirname(os.path.abspath(__file__))
path_image = os.path.join(base_dir, 'derstenatildik.jpg')
path_arrayencode = os.path.join(base_dir , 'afterbase64.txt')
path_arraydecode = os.path.join(base_dir , 'afterzlib.txt')

#image
image = Image.open(path_image)
gray_image = image.convert('L')
width, height = image.size

#numpy
np.set_printoptions(threshold=np.inf)
rgb_values = np.array(gray_image)
rgb_values_str = str(rgb_values)
print(rgb_values.shape)

#zlib
compress =zlib.compress(rgb_values_str.encode())

#base64
encoded = base64.b64encode(compress).decode()
decoded = base64.b64decode(encoded)


with open(path_arrayencode, mode = "w") as out_file:
    out_file.write(encoded)
with open(path_arraydecode, mode = "wb") as out_file:
    out_file.write(decoded)

'''
#qr
qr = qrcode.make(encoded)
qr.save("qrcode.png")  # QR kodu kaydet
'''





