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
import subprocess as SP
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready', 5000)
        self.setWindowTitle("Pick a file")
        self.setFixedWidth(950)
        self.setFixedHeight(500)
        self.setStyleSheet("background-color: white;");


        buttonCSS = "background-color: yellow; \
                border: 3px solid green; \
                font-size: 12pt;"
        buttonWidth = 100

        ##  Pick button ## 
        pickBTN = QPushButton(self)
        pickBTN.setText("Choose File")
        pickBTN.clicked.connect(self.open_dialog)
        pickBTN.setStyleSheet( buttonCSS )
        pickBTN.setMaximumWidth(buttonWidth)

        ##  copy button ## 
        copyBTN = QPushButton(self)
        copyBTN.setText("Copy File")
        copyBTN.clicked.connect(self.copy_file)
        copyBTN.setStyleSheet( buttonCSS )
        copyBTN.setMaximumWidth(buttonWidth)

        ## label ##
        self.NameLabel = QLabel()
        self.NameLabel.setText("NONE")
        self.NameLabel.setStyleSheet(
                "background-color: pink;"
                "border: 3px solid red;"
                "font-size: 12pt;")

        TitleButton = QLabel()
        TitleButton.setText("Pick File")
        TitleButton.setStyleSheet(
                "font-size: 14pt;"
                "font: bold;")
        TitleLabel = QLabel()
        TitleLabel.setText("File name:")
        TitleLabel.setStyleSheet(
                "font-size: 14pt;"
                "font: bold;")

        ## layout ##
        layout =QFormLayout()
        layout.setVerticalSpacing(33)
        layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addRow("",pickBTN)
        layout.addRow(TitleLabel,self.NameLabel)
        layout.addRow("",copyBTN)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        

    def copy_file(self):
        ## copy file to another directory ##
        command = "cp " + "'" + str(dirIn.text) + "/" + \
            str(self.NameLabel.text()) + "' " + str(dirOut.text) 
        SP.run(command, shell = True, executable="/bin/bash")
        self.statusBar().showMessage('File "' + \
                str(self.NameLabel.text()) + '" copied to dir ' + \
                str(dirOut.text), 3000)

    #@pyqtSlot()
    def open_dialog(self):
        self.statusBar().showMessage('Picking file...', 3000)
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            dirIn.text,
            "All Files (*);; Python Files (*.py);; PNG Files (*.png)",
        )
        filename = fname[0].split("/")[-1]
        self.NameLabel.setText(filename)

        self.statusBar().showMessage('Picked file "' + \
                str(filename) + '"', 3000)

if __name__ == "__main__":
    ## access config file**
    tree = ET.parse('config.xml')
    root = tree.getroot()
    dirIn = tree.find("dirIn")
    dirOut = tree.find("dirOut")

    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())
