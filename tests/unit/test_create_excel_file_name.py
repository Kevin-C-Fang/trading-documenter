# test_create_excel_file_name.py

import os
from datetime import datetime
from src.models.trading_documenter_model import TradingDocumenterModel


"""Tests the creation of the excel file name based on the current date"""

def test_if_create_excel_file_name_working():
    """_create_excel_file_name should match current date file name"""
    
    today = datetime.today().strftime("%m-%d-%Y")

    directory = "tests/unit/fixtures/" + today + "/"
    abs_path = os.path.abspath(directory + today + ".xlsx")

    assert TradingDocumenterModel._create_excel_file_name() == abs_path

    os.removedirs(directory)