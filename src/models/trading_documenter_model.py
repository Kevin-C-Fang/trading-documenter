# Filename: trading_documenter_model.py

"""
Prvoides TradingDocumenterModel, class for implement usage of data

TradingDocumenterModel implements the modeing of data for the application
"""

# Import os, datetime for creating excel name 
import os
from datetime import datetime

# Import openpyxl to create new/empty excel file
import openpyxl

# Import Pandas for create dataframe and saving to excel
import pandas as pd

class TradingDocumenterModel():
    """Class that implements the usage of data to be used in the application
    
    :param str directory: Path of folder that contains the xlsx and png of the day
    :param str AbsPath: Absolute path of the excel sheet
    """

    AbsPath = ""
    directory = ""

    def __init__(self) -> None:
        """Model Initializer"""

        self.options = {}
        self.options['strings_to_formulas'] = False
        self.options['strings_to_urls'] = False

        # Create abs path
        pre_path = "data/"
        folder_and_file_name = datetime.today().strftime("%m-%d-%Y")
        self.directory = pre_path + folder_and_file_name + "/"
        self.AbsPath = os.path.abspath(pre_path + folder_and_file_name + "/" + folder_and_file_name + ".xlsx")  

        self._create_excel_file_name()

    def _create_excel_file_name(self) -> str:
        """Creates excel file name and saves path as class property"""

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        # Use openpyxl to create empty excel file
        wb = openpyxl.Workbook()
        wb.save(self.AbsPath)

    def appendDataToExcel(self, data_dict: dict) -> None:
        """Appends dataframe to excel file"""

        # If file was deleted it will recreate
        if not os.path.exists(self.AbsPath):
            self._create_excel_file_name("data/")

        # Read in dataframes from excel and concat totgether to be written back to excel
        df_excel = pd.read_excel(self.AbsPath)
        data_frame = pd.DataFrame.from_dict([data_dict])
        result = pd.concat([df_excel, data_frame], ignore_index=True)

        with pd.ExcelWriter(self.AbsPath, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            result.to_excel(writer, sheet_name="Sheet", index=False)   
