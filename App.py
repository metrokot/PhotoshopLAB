'''

import sys
from PyQt5.Qt import *

from PIL import Image, ImageOps, ImageFilter
from PIL.ImageQt import ImageQt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        image  = Image.open("img/cat.jpg")
        image  = image.convert("RGBA")

        qim = ImageQt(image)

        self.pixmap = QPixmap(QImage(qim))
        label = QLabel()
        label.setPixmap(self.pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
'''