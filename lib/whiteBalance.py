from PIL import Image

class WhiteBalance:
    # Find the brightest point in the photo and get it's rgb value
    def __findBrightest(self):
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
    def __findAverage(self):
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

    # find the aboslute difference for rgb bands between brightest point in picture and white
    def whiteDeltasFixed(self):
        brightest = self.__findBrightest()
        R, G, B = 0, 1, 2
        white = (255, 255, 255)
        return (white[R] - brightest[R], white[G] - brightest[G], white[B] - brightest[B])

    # find the mulitplier for rgb bands difference between brightest point in picture and white
    def whiteMultipliers(self):
        brightest = self.__findBrightest()
        R, G, B = 0, 1, 2
        white = (255.0, 255.0, 255.0)
        return (white[R] / brightest[R], white[G] / brightest[G], white[B] / brightest[B])

    # find the aboslute difference for rgb bands between average point in picture and grey
    def neutralDeltas(self):
        average = self.__findAverage()
        R, G, B = 0, 1, 2
        grey = (127, 127, 127)
        return (grey[R] - average[R], grey[G] - average[G], grey[B] - average[B])

    # find the mulitplier for rgb bands ratio between average point in picture and grey
    def neutralMultipliers(self):
        average = self.__findAverage()
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
        self.updateLinearChange(mdeltas)

    # use average point in the photo to netural balance the photo by adding a fixed difference
    def neturalBalanceFixed(self):
        fdeltas = self.neutralDeltas()
        self.updateFixedChange(fdeltas)

    # use average point in the photo to netural balance the photo by a multiplier
    def neturalBalanceLinear(self):
        mdeltas = self.neutralMultipliers()
        self.updateLinearChange(mdeltas)

    # a combination of 50% white balance and 50% netura balance
    def balanceFixed(self):
        fWhiteDeltas = self.whiteDeltasFixed()
        fNeutralDeltas= self.neutralDeltas()
        fdeltas = tuple(map(lambda x, y: (x + y) / 2, fWhiteDeltas, fNeutralDeltas))
        self.updateFixedChange(fdeltas)

    def balanceLinear(self):
        mWhiteDeltas = self.whiteMultipliers()
        mNeutralDeltas = self.neutralMultipliers()
        mdeltas = tuple(map(lambda x, y: (x + y) / 2, mWhiteDeltas, mNeutralDeltas))
        self.updateLinearChange(mdeltas)
