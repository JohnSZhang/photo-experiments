from PIL import Image

class ColorShift:

    # Update current photo as an image made up of the supplied rgb bands
    def updatePhotoFromBands(self, bands):
        self.setPhoto(Image.merge(self.photo.mode, bands))

    # get rgb bands of current photo
    def currentBands(self):
        return self.getPhoto().split()

    # take an array of r g b values, apply to each of the rgb bands and set as current photo
    def updateFixedChange(self, deltas):
        imgSource = self.currentBands()
        R, G, B = 0, 1, 2
        red = imgSource[R].point(lambda i: max(0, min(i + deltas[R], 255)))
        green = imgSource[G].point(lambda i: max(0, min(i + deltas[G], 255)))
        blue = imgSource[B].point(lambda i: max(0, min(i + deltas[B], 255)))

        self.updatePhotoFromBands([red, green, blue])

    # take a series of multipliers for each of the RGB bands and applu
    def updateLinearChange(self, multipliers):
        imgSource = self.currentBands()
        R, G, B = 0, 1, 2
        red = imgSource[R].point(lambda i: max(0, min(i  * multipliers[R], 255)))
        green = imgSource[G].point(lambda i: max(0, min(i * multipliers[G], 255)))
        blue = imgSource[B].point(lambda i: max(0, min(i * multipliers[B], 255)))

        self.updatePhotoFromBands([red, green, blue])

    # add or subtract fixed delta to shift the photo red / blue
    def fwarmth(self, delta):
        if (abs(delta) > 100):
            raise Exception('Please enter a warmth delta between -100 and 100')

        self.updateFixedChange([delta, 0, delta * -1])

    # shifts tint of photo for a fixed amount between -100 and 100
    def ftint(self, delta):
        if (abs(delta) > 100):
            raise Exception('Please enter a tint delta between -100 and 100')

        self.updateFixedChange([0, delta, 0])

    # shifts the warmth of a photo by a multiplier between 0.3 and 2.0
    def mwarmth(self, multiplier):
        if (multiplier < 0.3 or multiplier > 2.0):
            raise Exception('Please enter a multipler between 0.3 and 2.0')

        self.updateLinearChange([multiplier, 1, (1 / multiplier)])

    # shifts tint of photo for a multiplier between 0.5 and 2
    def mtint(self, multiplier):
        if (multiplier < 0.5 or multiplier > 2.0):
            raise Exception('Please enter a multipler between 0.5 and 2.0')

        self.updateLinearChange([1, multiplier, 1 ])
