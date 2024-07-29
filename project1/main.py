#!/usr/bin/python3
import sys
from PyQt6.QtWidgets import QApplication
from mvp.model import Model
from mvp.view import MyDialog
from mvp.presenter import Presenter

def main():
    app = QApplication(sys.argv)
    
    model = Model()
    view = MyDialog()
    presenter = Presenter(model, view)  # This implicitly ties model and view together
    
    view.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
