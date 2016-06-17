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

    # use brightest point in the photo to white balance the photo by adding a fixed difference
    def whiteBalanceFixed(self):
        brightest = self.__findBrightest()
        R, G, B = 0, 1, 2
        white = (255, 255, 255)
        fdeltas = (white[R] - brightest[R], white[G] - brightest[G], white[B] - brightest[B])
        self.updateFixedChange(fdeltas)

    # use brightest point in the photo to white balance the photo linearly
    def whiteBalanceLinear(self):
        brightest = self.__findBrightest()
        R, G, B = 0, 1, 2
        white = (255.0, 255.0, 255.0)
        mdeltas = (white[R] / brightest[R], white[G] /  brightest[G], white[B] / brightest[B])
        self.updateLinearChange(mdeltas)

    # use average point in the photo to netural balance the photo by adding a fixed difference
    def neturalBalanceFixed(self):
        average = self.__findAverage()
        R, G, B = 0, 1, 2
        grey = (127, 127, 127)
        fdeltas = (grey[R] - average[R], grey[G] - average[G], grey[B] - average[B])
        self.updateFixedChange(fdeltas)

    # use average point in the photo to netural balance the photo by a multiplier
    def whiteBalanceLinear(self):
        average = self.__findAverage()
        R, G, B = 0, 1, 2
        grey = (127, 127, 127)
        mdeltas = (grey[R] / average[R], grey[G] /  average[G], grey[B] / average[B])
        self.updateLinearChange(mdeltas)
