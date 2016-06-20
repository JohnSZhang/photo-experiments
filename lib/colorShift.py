from PIL import Image

class ColorShift:
    # take an array of r g b values, apply to each of the rgb bands and set as current photo
    def __updateFixedChange(self, deltas):
        R, G, B = 0, 1, 2
        red = lambda i: max(0, min(i + deltas[R], 255))
        green = lambda i: max(0, min(i + deltas[G], 255))
        blue = lambda i: max(0, min(i + deltas[B], 255))

        self.__rgbUpdate(red, green, blue)

    # take a series of multipliers for each of the RGB bands and applu
    def __updateLinearChange(self, multipliers):
        R, G, B = 0, 1, 2
        red = lambda i: max(0, min(i  * multipliers[R], 255))
        green = lambda i: max(0, min(i * multipliers[G], 255))
        blue = lambda i: max(0, min(i * multipliers[B], 255))

        self.__rgbUpdate(red, green, blue)


    # add or subtract fixed delta to shift the photo red / blue
    def fwarmth(self, delta):
        self.ensureMode('RGB')
        if (abs(delta) > 100):
            raise Exception('Please enter a warmth delta between -100 and 100')

        self.__updateFixedChange([delta, 0, delta * -1])

    # shifts tint of photo for a fixed amount between -100 and 100
    def ftint(self, delta):
        self.ensureMode('RGB')
        if (abs(delta) > 100):
            raise Exception('Please enter a tint delta between -100 and 100')

        self.__updateFixedChange([0, delta, 0])

    # shifts the warmth of a photo by a multiplier between 0.3 and 2.0
    def mwarmth(self, multiplier):
        self.ensureMode('RGB')
        if (multiplier < 0.3 or multiplier > 2.0):
            raise Exception('Please enter a multipler between 0.3 and 2.0')

        self.__updateLinearChange([multiplier, 1, (1 / multiplier)])

    # shifts tint of photo for a multiplier between 0.5 and 2
    def mtint(self, multiplier):
        self.ensureMode('RGB')
        if (multiplier < 0.5 or multiplier > 2.0):
            raise Exception('Please enter a multipler between 0.5 and 2.0')

        self.__updateLinearChange([1, multiplier, 1 ])

    # changes the contrast of the photo by a factor
    def contrast(self, delta):
        self.ensureMode('RGB')
        # raise exception if contrast isn't within acceptable range
        if (delta < -1 or delta > 1):
            raise Exception('Please enter a contrast change between -1 and 1')
        # upates luma with the rgb -> luma conversation from http://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color
        # Y = 0.299 R + 0.587 G + 0.114 B
        red = lambda x: max(0, min(255, (delta * (0.299) * x) + x))
        green = lambda x: max(0, min(255, (delta * (0.587) * x) + x))
        blue = lambda x: max(0, min(255, (delta * (0.114) * x) + x))

        self.__rgbUpdate(red, green, blue)

    # update photo with given point transform functions
    def __rgbUpdate(self, rUpate, gUpdate, bUpdate):
        #get bands
        bands = self.getPhoto().split()
        R, G, B = 0, 1, 2
        defaultUpdate = lambda x: x

        #Apply RGB bands in sequene
        red = bands[R].point(rUpate or defaultUpdate)
        green = bands[G].point(gUpdate or defaultUpdate)
        blue = bands[B].point(bUpdate or defaultUpdate)
        self.updatePhotoFromBands('RGB', [red, green, blue])
