# test_create_excel_file_name.py

import os
from datetime import date
from src.models.trading_documenter_model import TradingDocumenterModel


"""Tests the creation of the excel file name based on the current date"""

def test_if_create_excel_file_name_working():
    """_create_excel_file_name should match current date file name"""
    today = date.today()

    formated_date = today.strftime("%d-%m-%Y")
    abs_path = os.path.abspath("data/" + formated_date + ".xlsx")

    assert TradingDocumenterModel._create_excel_file_name() == abs_path