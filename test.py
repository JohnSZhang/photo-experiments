from PIL import Image
from lib.latergram import Latergram

img = Image.open('photo/peacock.jpg')

latergram = Latergram(img)
latergram.mtint(1.2)
latergram.show()
latergram.setOriginalPhoto()
latergram.ftint(20)
latergram.show()
