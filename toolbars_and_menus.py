#!/usr/bin/python3
import os
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
        QApplication, 
        QLabel,
        QMainWindow,
        QStatusBar,
        QToolBar,
        QCheckBox
    )

basedir = os.path.dirname(__file__)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #sipPyTypeDictRef().__init__()

        self.setWindowTitle("Toolbars and Menus")


        ##### label ######
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        #####

        # button Action#
        button_action = QAction(
                QIcon(os.path.join(basedir,"bug.png")),
                "&Your button",
                self
                )
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick) 
        button_action.setCheckable(True)
        ##############

        # button Action2#
        button_action2 = QAction(
                QIcon(os.path.join(basedir,"bug.png")),
                "Your &button2", 
                self
                )
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick) 
        button_action2.setCheckable(True)
        #################

        ###### Toolbar #######################
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(
                Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)

        ## add buttons to toolbar
        toolbar.addAction(button_action)
        toolbar.addSeparator()
        toolbar.addAction(button_action2)
        ###########

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox())
       
        #########################################

        ##  Status Bar##
        self.setStatusBar(QStatusBar(self))


        ###  Menu ###############################
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        ###########################################

    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)


app = QApplication(sys.argv)
app.setStyle('Fusion')


window = MainWindow()
window.show()

app.exec()

