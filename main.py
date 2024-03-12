from PIL import Image, ImageDraw

'''
Изображение 1
prct2
'''
image = Image.open('prct2.jpeg', mode='r')  # Открываем изображение
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей
'''
Изображение 2
prct3
'''
image2 = Image.open('prct3.jpeg', mode='r')  # Открываем изображение
pix2 = image2.load()  # Выгружаем значения пикселей


draw = ImageDraw.Draw(image)

def checkLimit(number):
    if (number>255):
        return 255
    else:
        return number


def summ(): #сумма 2изображений по пиксельно до 255
    for x in range(width):
        for y in range(height):
            draw.point((x, y), (checkLimit(pix[x, y][0] + pix2[x, y][0]), checkLimit(pix[x, y][1] + pix2[x, y][1]), checkLimit(pix[x, y][2] + pix2[x, y][2])))
            #print(x,y)
def srAr():# ср арифм 2 изображений и округлять до целого
    for x in range(width):
        for y in range(height):
            r = (pix[x, y][0] + pix2[x, y][0]) // 2
            g = (pix[x, y][1] + pix2[x, y][1]) // 2
            b = (pix[x, y][2] + pix2[x, y][2]) // 2
            draw.point((x, y), (r, g, b))
def maximum():# попиксельный максиум
    for x in range(width):
        for y in range(height):
            draw.point((x,y), (max(pix[x, y][0], pix2[x, y][0]),max(pix[x, y][1], pix2[x, y][1]),max(pix[x, y][2], pix2[x, y][2])))


summ()
image.save("result.jpg", "JPEG")
#image.show()
srAr()
image.save("result2.jpg", "JPEG")
#image.show()
maximum()
image.save("result3.jpg", "JPEG")
#image.show()

