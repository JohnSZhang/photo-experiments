from PIL import Image

img = Image.open('photo/peacock.jpg')

# print(img.format, img.size, img.mode)
img.point(lambda a: print(a))
#
img.show();
imgSource = img.split()

R, G, B = 0, 1, 2

red = imgSource[R].point(lambda i: min(i, 255))

green = imgSource[G].point(lambda i: min(i, 255))

blue = imgSource[B].point(lambda i: min(i + 55, 255))

# paste the processed band back, but only where red was < 100
# source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(img.mode, [red, green, blue])
im.show()
