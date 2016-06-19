from PIL import Image

class Saturation:
    # shifts the hue of a photo by the specified degree
    def hueUpdate(self, degree):
        # raise error if degree is not in acceptable range
        if (degree < 0 or degree > 360):
            raise Exception('Please select a hue degree between 0 and 360')
        degreeInBits = degree / 360 * 255
        # get hue update function and apply to photo
        hueUpdate = lambda x: (x + degreeInBits + 255) % 255
        self.__hsvUpdate(hueUpdate, 0, 0)

    # shifts the satuation of the photo by a set amount
    def saturationUpdate(self, delta):
        # raise error if delta is not in acceptable range
        if (delta < -255 or delta > 255):
            raise Exception('Please select a saturation change between 0 and 255')

        # create saturation update function and apply to photo
        saturationUpdate = lambda x: max(min(x + delta, 255), 0)
        self.__hsvUpdate(0, saturationUpdate, 0)

    # shifts the value of the photo by a set amount
    def valueUpdate(self, delta):
        # raise error if delta is not in acceptable range
        if (delta < -255 or delta > 255):
            raise Exception('Please select a value change between 0 and 255')

        # create saturation update function and apply to photo
        valueUpdate = lambda x: max(min(x + delta, 255), 0)
        self.__hsvUpdate(0, 0, valueUpdate)

    # updates HSV values of the photo with provided update functions
    def __hsvUpdate(self, hUpdate, sUpdate, vUpdate):
        self.ensureMode('HSV')
        #get bands
        bands = self.getPhoto().split()
        H, S, V = 0, 1, 2
        defaultUpdate = lambda x: x

        #update hsv values by band
        hue = bands[H].point(hUpdate or defaultUpdate)
        saturation = bands[S].point(sUpdate or defaultUpdate)
        value = bands[V].point(vUpdate or defaultUpdate)
        self.updatePhotoFromBands('HSV', [hue, saturation, value])

    # turns photo into pastal version
    def pastalify(self):
        return 0
