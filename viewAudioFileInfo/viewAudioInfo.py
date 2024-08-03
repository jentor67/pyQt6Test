#!/usr/bin/python3
from PyQt6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QPushButton, 
    QFileDialog,
    QFormLayout,
    QLabel,
    QWidget,
    QTableView
)
from PyQt6.QtCore import Qt, pyqtSlot, QAbstractTableModel
import sys
import xml.etree.ElementTree as ET
import subprocess as SP
import pandas as pd
from tableModel import TableModel
from audioProbeDF import AudioDataFrame
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready', 5000)
        self.setWindowTitle("Pick a file")
        self.setFixedWidth(1500)
        self.setFixedHeight(750)
        self.setStyleSheet("background-color: white;");


        buttonCSS = "background-color: yellow; \
                border: 3px solid green; \
                font-size: 12pt;"
        buttonWidth = 150

        ##  Pick button ## 
        pickBTN = QPushButton(self)
        pickBTN.setText("Choose Folder")
        pickBTN.clicked.connect(self.open_dialog)
        pickBTN.setStyleSheet( buttonCSS )
        pickBTN.setMaximumWidth(buttonWidth)

        ##  copy button ## 
        copyBTN = QPushButton(self)
        copyBTN.setText("View Info")
        self.folder ="" #"/home/jmajor/Music/Boy2"
        copyBTN.clicked.connect(lambda: self.view_info(self.folder))
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

        ## Create QTableView
        self.table = QTableView()
        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)
        #self.table.setColumnWidth(1,150)

        ## layout ##
        self.layout =QFormLayout()
        self.layout.setVerticalSpacing(33)
        self.layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.addRow("",pickBTN)
        self.layout.addRow(TitleLabel,self.NameLabel)
        self.layout.addRow("",copyBTN)
        self.layout.addRow("",self.table)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)


    def view_info(self,searchFolder):
        ## view info of audio files in folder ##

        ## call AudioDataFrame class
        self.audioDF = AudioDataFrame()

        ## create data frame for folder ##
        data = self.audioDF.getDataFrame(searchFolder)
       
        self.model = TableModel(data)

        ## populate self.table with self.model ##
        self.table.setModel(self.model)
        self.table.setColumnWidth(0,300)

    #@pyqtSlot()
    def open_dialog(self):
        self.statusBar().showMessage('Picking a folder...', 3000)
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Directory",
            directory="/home/jmajor/Music"
        )
        self.folder=folder

        self.statusBar().showMessage('Picked folder "' + \
                str(folder) + '"', 3000)

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
