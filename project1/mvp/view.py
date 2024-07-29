#!/usr/bin/python3

from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import pyqtSignal
from typing import Dict

class MyDialog(QDialog, Ui_Dialog):
    input_data_collected = pyqtSignal(dict)

    def on_start_clicked(self) -> None:
        data_dict: Dict[str, str] = {
            'inputEdit1': self.lineEdit1.text(),
            # ... Add more input fields as needed ...
        }
        self.input_data_collected.emit(data_dict)
