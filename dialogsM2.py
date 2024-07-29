#!/usr/bin/python3
import sys
from PyQt6.QtWidgets import (
        QApplication,
        QMainWindow, 
        QMessageBox,
        QPushButton
    )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message Box")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, is_checked):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        dlg.setStandardButtons(
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No
                )
        dlg.setIcon(QMessageBox.Icon.Question)

        button = dlg.exec()

        button = QMessageBox.StandardButton(button)

        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()





