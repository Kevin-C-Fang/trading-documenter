# Filename: trading_documenter_model.py

"""
Prvoides TradingDocumenterModel, class for implement usage of data

TradingDocumenterModel implements the modeing of data for the application
"""

# Import os, datetime for creating excel name 
import os
from datetime import datetime

# Import Pandas for create dataframe and savingin to excel
import pandas as pd

class TradingDocumenterModel():
    """Class that implements the usage of data to be used in the application
    
    :param str _abs_path: Absolute path of the excel sheet
    """

    def __init__(self) -> None:
        """Model Initializer"""

        self._create_excel_file_name()

    def _create_excel_file_name(self) -> str:
        """Creates excel file name and saves as class property"""

        today = datetime.today().strftime("%m-%d-%Y")
        specified_time_and_date = datetime.now().strftime("%m-%d-%Y, %H-%M-%S")
        self._abs_path = os.path.abspath("data/" + today + "/" + specified_time_and_date + ".xlsx")  

    def appendDataToExcel(data_dict: dict) -> None:
        pass