from PIL import Image
from lib.latergram import Latergram

img = Image.open('photo/kyoto.jpg')

latergram = Latergram(img)
# latergram.show()
# latergram.fwarmth(-50)
# latergram.show()
# latergram.setOriginalPhoto()
# latergram.mwarmth(1.6)
# latergram.show()
# latergram.setOriginalPhoto()
# latergram.mwarmth(0.4)
# latergram.show()
# latergram.whiteBalanceFixed()
# latergram.show()
# latergram.setOriginalPhoto()
# latergram.whiteBalanceLinear()
# latergram.show()
# average = latergram.findAverage()
# fdeltas = (127 - average[0], 127 - average[1], 127 - average[2])
# latergram.updateFixedChange(fdeltas)
# print(fdeltas)
# latergram.show()
# img2 = Image.open('photo/kyoto.jpg')
# latergram = Latergram(img2)
# latergram.whiteBalanceFixed()
# latergram.show()
latergram.show()
latergram.whiteBalanceLinear()
latergram.show()
latergram.setOriginalPhoto()
latergram.neturalBalanceFixed()
latergram.show()
