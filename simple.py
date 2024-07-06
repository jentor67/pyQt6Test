#!/usr/bin/python3

"""
ZetCode PyQt6 tutorial

In this example, we create a simple
window in PyQt6.

Author: Jan Bodnar
Website: zetcode.com
"""


import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 200)
    w.move(90, 300)

    w.setWindowTitle('Hello Simple')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
