# Filename: trading_documenter_controller.py

"""Provides TradingDocumenterController, class for connecting the view to modeling

TradingDocumenterController implements the events for the controls of the view using event handlers which pass information to the modeling.
"""

# Import QtWidgets for type comparison
from PyQt5.QtWidgets import (QLineEdit, QCheckBox)

# Import view and model to access functions
from models.trading_documenter_model import TradingDocumenterModel
from views.trading_documenter_view import TradingDocumenterView


class TradingDocumenterController:
    """Class that implements the connection between the View and Model in the Model-View-Controler(MVC) design pattern.
    
    :param TradingDocumenterView view: instance of this TradingDocumenterView
    :param TradingDocumenterModel model: instance of this TradingDocumenterModel
    """

    def __init__(self, model_Obj: TradingDocumenterModel, view_Obj: TradingDocumenterView) -> None:
        """Controller Initializer"""
        
        self.view = view_Obj
        self.model = model_Obj

        self.connect_signals()

    def connect_signals(self):
        """Connects the buttons to invoking methods"""
        
        self.view.EnterAndClearButtons[0].clicked.connect(lambda: self._enter_button_clicked())
        self.view.EnterAndClearButtons[1].clicked.connect(lambda: self._clear_button_clicked())
        self.view.Options[-1].clicked.connect(lambda: self._screenshot_button_clicked())

    def _screenshot_button_clicked(self):
        """Screenshot button event function which is used to capture and pass screenshot to modeling"""
        
        self.view.takeScreenshot()

    def _enter_button_clicked(self):
        """Enter button event function which is to pass data to modeling"""
        
        data_dict = self._generate_dict_of_data()

        self.model.appendDataToExcel(data_dict)
        self.view.clearAllValues()

    def _generate_dict_of_data(self) -> dict:
        """Generates the data from the values entered into the view"""

        combined_dict = {}

        for option in self.view.Options:
            if type(option) == QCheckBox:
                combined_dict[option.text()] = "???" if option.isChecked() == True else "???"
            if type(option) == QLineEdit:
                combined_dict["Risk:Reward"] = option.text()

        combined_dict["Notes"] = self.view.Notes.toPlainText()
        combined_dict["Path"] = self.view.ScreenshotPath

        return combined_dict

    def _clear_button_clicked(self):
        """Clear button event function which is to clear all data currently entered"""
        
        self.view.clearAllValues()