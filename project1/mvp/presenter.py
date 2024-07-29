#!/usr/bin/python3

from typing import Dict

class Presenter:
    def __init__(self, model: Model, view: MyDialog) -> None:
        self.model = model
        self.view = view
        self.view.input_data_collected.connect(self.handle_input_data)

    def handle_input_data(self, data_dict: Dict[str, str]) -> None:
        self.model.set_input_data(data_dict)
        print(data_dict)
