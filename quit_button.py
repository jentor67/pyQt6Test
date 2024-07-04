#!/usr/bin/python3

"""
ZetCode PyQt6 tutorial

This program creates a quit
button. When we press the button,
the application terminates.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtWidgets import (QWidget, QToolTip, 
        QPushButton, QApplication)

from PyQt6.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>Quit widget</b>')

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('Just click to <b>Quit</b> dummy')

        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Quit button')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
