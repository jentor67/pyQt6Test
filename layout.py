#!/usr/bin/python3
import sys
from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QPalette, QColor



class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
       

class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.resize(900,500)
        self.move(90,300)


        layoutH = QHBoxLayout()
        layoutH.addWidget(Color('yellow'))
        layoutH.addWidget(Color('purple'))


        layoutV = QVBoxLayout()
        layoutV.addLayout(layoutH)

        layoutV.addWidget(Color('red'))
        layoutV.addWidget(Color('green'))
        layoutV.addWidget(Color('blue'))


        widget = QWidget()
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
