#!/usr/bin/python3
from PyQt6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QPushButton, 
    QFileDialog,
    QFormLayout,
    QLabel,
    QWidget
)
from PyQt6.QtCore import Qt, pyqtSlot
import sys
import xml.etree.ElementTree as ET
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pick a file")
        self.setFixedWidth(750)
        self.setFixedHeight(500)
        self.setStyleSheet("background-color: white;");

        layout =QFormLayout()
        layout.setVerticalSpacing(33)
        layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        
        btn = QPushButton(self)
        btn.setText("Open file dialog")
        self.setCentralWidget(btn)
        btn.clicked.connect(self.open_dialog)
        btn.setStyleSheet(
                "background-color: yellow;"
                "border: 3px solid green;");

        self.NameLabel = QLabel()
        self.NameLabel.setText("NONE")
        self.NameLabel.setStyleSheet(
                "background-color: pink;"
                "border: 3px solid red;");

        layout.addRow("Pick File",btn)
        layout.addRow("File name: ",self.NameLabel)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        


    #@pyqtSlot()
    def open_dialog(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            dirIn.text,
            "All Files (*);; Python Files (*.py);; PNG Files (*.png)",
        )
        print(fname)
        self.NameLabel.setText(fname[0])

if __name__ == "__main__":
    ## access config file**
    tree = ET.parse('config.xml')
    root = tree.getroot()
    dirIn = tree.find("dirIn")
    dirOut = tree.find("dirOut")
    print(dirIn.text)

    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())
