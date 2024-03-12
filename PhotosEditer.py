'''
Попиксельная сумма
произведение(умножение на цвет пикселя изображения деленный на 255)
среднее арифм
минимум, максимум

(наложить) умножить на изображение маску(форма маски круг, квадрат, прямоугольник)

возможность ввести название файла для сохранения
'''

'''
Разный размер изображений

можно выбрать цветовые каналы(галочками) с каким цветом работать 
^^^
|||
Python PIL | Image.split() method

для попиксельных операций меньшее изображение должно воздействать на всё большее изображение то есть растянуть
Image.resize()

'''
from PIL import Image, ImageDraw


class Photos:
    photo = [] #item - индексация
    def __add__(self, photoName):
        self.photo+=(Image.open(photoName, mode='r'))
    def __delitem__(self, item): # del Photo[1]
        self.photo.remove(item)
    def __getitem__(self, item): #Photo[2]
        return self.photo[item]
    def __call__(self, *args, **kwargs):
        pass
    def sum(self,items):
        pass
    def srAr(self,items):
        pass
    def mimimum(self,items):
        pass
    def maximum(self,items):
        pass
    def multiplay(self,items):
        pass

