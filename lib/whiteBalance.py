from PIL import Image

class WhiteBalance:
    # Find the brightest point in the photo and get it's rgb value
    def findBrightest(self):
        imgSource = self.getPhoto().split()
        sourceList = list(map(lambda color: imgSource[color].getdata(), [0, 1, 2]))

        maxSum = 0
        brightest = None

        # for i in range(0, len(sourceList[1]) - 1):
        for i in range(0, len(sourceList[1]) - 1):
            R, G, B = sourceList[0][i], sourceList[1][i], sourceList[2][i]
            sum = R + G + B
            if (sum > maxSum):
                maxSum = sum
                brightest = (sourceList[0][i], sourceList[1][i], sourceList[2][i])

        print(brightest)
        brightest
