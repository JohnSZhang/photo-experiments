from PIL import Image
from lib.latergram import Latergram

img = Image.open('photo/whiteadjust.jpg')

latergram = Latergram(img)
latergram.findBrightest()
