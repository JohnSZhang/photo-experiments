from PIL import Image
from lib.latergram import Latergram

img = Image.open('photo/kyoto.jpg')

latergram = Latergram(img)
latergram.show()
latergram.applyColor(4500)
latergram.show()
