# Filename: trading_documenter_model.py

"""
Prvoides TradingDocumenterModel, class for implement usage of data

TradingDocumenterModel implements the modeing of data for the application
"""

import os
from datetime import date
from typing import Callable

class TradingDocumenterModel():
    """Class that implements the usage of data to be used in the application
    
    """

    def __init__(self, createMessageBox: Callable=print):
        
        self._create_excel_file_name()

    def _create_excel_file_name(self):
        today = date.today()

        formated_date = today.strftime("%d-%m-%Y")
        abs_path = os.path.abspath("data/" + formated_date + ".xlsx")