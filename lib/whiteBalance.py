from PIL import Image
from math import log

class WhiteBalance:
    # find the aboslute difference for rgb bands between brightest point in picture and white
    def whiteDeltasFixed(self):
        brightest = self.__brightestPoint()
        R, G, B = 0, 1, 2
        white = (255, 255, 255)
        return (white[R] - brightest[R], white[G] - brightest[G], white[B] - brightest[B])

    # find the mulitplier for rgb bands difference between brightest point in picture and white
    def whiteMultipliers(self):
        brightest = self.__brightestPoint()
        R, G, B = 0, 1, 2
        white = (255.0, 255.0, 255.0)
        return (white[R] / brightest[R], white[G] / brightest[G], white[B] / brightest[B])

    # find the aboslute difference for rgb bands between average point in picture and grey
    def neutralDeltas(self):
        average = self.__averagePoint()
        R, G, B = 0, 1, 2
        grey = (127, 127, 127)
        return (grey[R] - average[R], grey[G] - average[G], grey[B] - average[B])

    # find the mulitplier for rgb bands ratio between average point in picture and grey
    def neutralMultipliers(self):
        average = self.__averagePoint()
        R, G, B = 0, 1, 2
        grey = (127.0, 127.0, 127.0)
        return (grey[R] / average[R], grey[G] / average[G], grey[B] / average[B])

    # use brightest point in the photo to white balance the photo by adding a fixed difference
    def whiteBalanceFixed(self):
        fdeltas = self.whiteDeltasFixed()
        self.updateFixedChange(fdeltas)

    # use brightest point in the photo to white balance the photo linearly
    def whiteBalanceLinear(self):
        mdeltas = self.whiteMultipliers()
        self.__updateLinearChange(mdeltas)

    # use average point in the photo to netural balance the photo by adding a fixed difference
    def neturalBalanceFixed(self):
        fdeltas = self.neutralDeltas()
        self.updateFixedChange(fdeltas)

    # use average point in the photo to netural balance the photo by a multiplier
    def neturalBalanceLinear(self):
        mdeltas = self.neutralMultipliers()
        self.__updateLinearChange(mdeltas)

    # a combination of 50% white balance and 50% netura balance with fixed difference
    def balanceFixed(self):
        fWhiteDeltas = self.whiteDeltasFixed()
        fNeutralDeltas= self.neutralDeltas()
        fdeltas = tuple(map(lambda x, y: (x + y) / 2, fWhiteDeltas, fNeutralDeltas))
        self.updateFixedChange(fdeltas)

    # a combination of 50% white balance and 50% netura balance with linear scale
    def balanceLinear(self):
        mWhiteDeltas = self.whiteMultipliers()
        mNeutralDeltas = self.neutralMultipliers()
        mdeltas = tuple(map(lambda x, y: (x + y) / 2, mWhiteDeltas, mNeutralDeltas))
        self.__updateLinearChange(mdeltas)

    # returns copy of photo with given color temperature linearlys scaled
    def applyColor(self, temperature):
        R, G, B = 0, 1, 2
        # take temperature, and get the associated Black-body radiation color
        bBodyColor= self.__blackBodyColor(temperature)

        # get the current color of brightest point in photo
        brightest = self.__brightestPoint()
        # get ratio of difference between expect color and brightest point
        ratios = (bBodyColor[R] / brightest[R], bBodyColor[G] / brightest[G], bBodyColor[B] / brightest[B])

        self.__updateLinearChange(ratios)

    # Find the brightest point in the photo and get it's rgb value
    def __brightestPoint(self):
        self.ensureMode('RGB')
        imgSource = self.getPhoto().split()
        sourceList = list(map(lambda color: imgSource[color].getdata(), [0, 1, 2]))

        maxSum = 0
        brightest = None

        for i in range(0, len(sourceList[1]) - 1):
            R, G, B = sourceList[0][i], sourceList[1][i], sourceList[2][i]
            sum = R + G + B
            if (sum > maxSum):
                maxSum = sum
                brightest = (sourceList[0][i], sourceList[1][i], sourceList[2][i])

        return brightest

    # find the color of the average point in the photo
    def __averagePoint(self):
        self.ensureMode('RGB')
        imgSource = self.getPhoto().split()
        sourceList = list(map(lambda color: imgSource[color].getdata(), [0, 1, 2]))

        bandlength = len(sourceList[1])
        sums = [0, 0, 0]
        R, G, B = 0, 1, 2
        for i in range(0, bandlength - 1):
            sums[R] += sourceList[R][i]
            sums[G] += sourceList[G][i]
            sums[B] += sourceList[B][i]

        average = tuple(map(lambda x: x / bandlength, sums))
        return average

    # sets a color within the acceptable color range
    def __correctRange(self, color):
        return  max(0, min(color, 255))

    # returns black body color of a particular temperature in kelvin, see http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/ for algorithm source
    def __blackBodyColor(self, temp):
        # throw error if temp is not within bound range
        if (temp < 1000 or temp > 40000):
            raise Exception('Invalid temperature, please enter a temperature between 1000 and 40000!')

        # initialize
        temp = temp / 100
        red, green, blue = (255, 255, 255)

        #calculate red
        if temp <= 66:
            red = 255
        else:
            red = 329.698727446 * ((temp - 60) ** -0.133204)

        #calculate green
        if temp <= 66:
            green = log(temp) * 99.47080 - 161.1195
        else:
            green = 288.12216 * ((temp - 60) ** -0.075514)

        #calculate blue
        if temp >= 66:
            blue = 255
        elif temp <= 19:
            blue = 0
        else:
            blue = log(temp - 10) * 138.517731  - 305.044792

        red = self.__correctRange(red)
        green = self.__correctRange(green)
        blue = self.__correctRange(blue)
        return (red, green, blue)
