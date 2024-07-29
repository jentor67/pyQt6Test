#!/usr/bin/python3

import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():


    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    w = QWidget()
    w.resize(500, 200)
    w.move(90, 300)
    w.setWindowTitle('Hello Simple')
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
