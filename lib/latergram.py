from PIL import Image

class Latergram:
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

    # add or subtract fixed delta to shift the photo red / blue
    def fwarmth(self, delta):
        if (abs(delta) > 100):
            raise Exception('Please enter a warmth delta between -100 and 100')

        imgSource = self.photo.split();
        R, G, B = 0, 1, 2

        red = imgSource[R].point(lambda i: max(0, min(i + delta, 255)))
        green = imgSource[G]
        blue = imgSource[B].point(lambda i: max(0, min(i - delta, 255)))

        self.photo = Image.merge(self.photo.mode, [red, green, blue])

    # shifts the warmth of a photo by a multiplier between 0.5 and 2.0
    def mwarmth(self, multiplier):
        if (multiplier < 0.5 or multiplier > 2.0):
            raise Exception('Please enter a multipler between 0.5 and 2.0')
        imgSource = self.photo.split();
        R, G, B = 0, 1, 2

        red = imgSource[R].point(lambda i: max(0, min(i * multiplier, 255)))
        green = imgSource[G]
        blue = imgSource[B].point(lambda i: max(0, min(i * (1 / multiplier), 255)))

        self.photo = Image.merge(self.photo.mode, [red, green, blue])

    # shifts tint of photo for a fixed amount between -100 and 100
    def ftint(self, delta):
        if (abs(delta) > 100):
            raise Exception('Please enter a tint delta between -100 and 100')

        imgSource = self.photo.split();
        R, G, B = 0, 1, 2

        red = imgSource[R]
        green = imgSource[G].point(lambda i: max(0, min(i + delta, 255)))
        blue = imgSource[B]

        self.photo = Image.merge(self.photo.mode, [red, green, blue])

    # shifts tint of photo for a multiplier between 0.5 and 2
    def mtint(self, multiplier):
        if (multiplier < 0.5 or multiplier > 2.0):
            raise Exception('Please enter a multipler between 0.5 and 2.0')

        imgSource = self.photo.split();
        R, G, B = 0, 1, 2

        red = imgSource[R]
        green = imgSource[G].point(lambda i: max(0, min(i * multiplier, 255)))
        blue = imgSource[B]

        self.photo = Image.merge(self.photo.mode, [red, green, blue])
