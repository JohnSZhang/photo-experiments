from PIL import Image
from lib.colorShift import ColorShift
from lib.whiteBalance import WhiteBalance
from lib.saturation import Saturation

class Latergram(ColorShift, WhiteBalance, Saturation):
    # latergram can be instantiated with a photo
    def __init__(self, photo = None):
        self.photo = photo
        self.originalPhoto = photo

    # ensures a photo exists for the latergram, else raise error
    def ensurePhoto(self):
        if (not self.photo):
            raise Exception('You did not include a photo to latergram!')

    # sets the photo of current latergram
    def setPhoto(self, photo):
        self.photo = photo

    # sets the current photo as well as the original photo
    def resetPhoto(self, photo):
        self.setPhoto(photo)
        self.originalPhoto = photo

    # returns the photo of current latergram
    def getPhoto(self):
        self.ensurePhoto()
        return self.photo

    # resets photo to the original one
    def setOriginalPhoto(self):
        if (not self.originalPhoto):
            raise Exception('You do not have an original photo to reset to!')
        self.photo = self.originalPhoto

    # get rgb bands of current photo
    def currentBands(self):
        return self.getPhoto().split()

    # Update current photo as an image made up of the supplied rgb bands
    def updatePhotoFromBands(self, mode, bands):
        self.setPhoto(Image.merge(mode, bands))

    # display current latergram photo to user
    def show(self):
        self.ensurePhoto()
        self.photo.show()

    # update mode of image
    def ensureMode(self, mode):
        if ['HSV', 'RGB'].count(mode) == 0:
            raise Exception('Not a support image mode')
        if (not self.photo.mode == mode):
            self.setPhoto( self.photo.convert(mode))
