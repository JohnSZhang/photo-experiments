from PIL import Image
from lib.colorShift import ColorShift

class Latergram(ColorShift):
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
        self.originalPhoto = photo

    # returns the photo of current latergram
    def getPhoto(self):
        self.ensurePhoto()
        return self.photo

    # resets photo to the original one
    def setOriginalPhoto(self):
        self.photo = self.originalPhoto

    # display current latergram photo to user
    def show(self):
        self.ensurePhoto()
        self.photo.show()
