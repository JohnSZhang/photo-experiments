from PIL import Image
from lib.latergram import Latergram

img = Image.open('photo/kyoto.jpg')

latergram = Latergram(img)
latergram.show()
latergram.whiteBalanceFixed()
latergram.show()
latergram.setOriginalPhoto()
latergram.neturalBalanceFixed()
latergram.show()
latergram.setOriginalPhoto()
latergram.balanceFixed()
latergram.show()
