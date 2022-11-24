import sys

from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        self.do_paint = True
        n = randrange(10, 20)
        for i in range(n):
            qp.setBrush(QColor(randrange(256), randrange(256), randrange(256)))
            d = randrange(50)
            qp.drawEllipse(randrange(400 - d), randrange(400 - d), d, d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
