# test_create_excel_file_name.py

import os, shutil
from datetime import datetime

from src.models.trading_documenter_model import TradingDocumenterModel

"""Tests the creation of the excel file name based on the current date"""

model = TradingDocumenterModel()

def get_pre_path():
    return "tests/unit/fixtures/"

def get_Abs_Path():
    pre_path = get_pre_path()
    folder_and_file_name = datetime.today().strftime("%m-%d-%Y")

    model.directory = pre_path + folder_and_file_name + "/"
    model.AbsPath = os.path.abspath(pre_path + folder_and_file_name + "/" + folder_and_file_name + ".xlsx")

    return model.AbsPath

def test_if_create_excel_file_name_working():
    """_create_excel_file_name should match current date file name"""

    abs_path = get_Abs_Path()

    model._create_excel_file_name()

    assert os.path.exists(abs_path) == True

    shutil.rmtree(get_pre_path() + datetime.today().strftime("%m-%d-%Y") + "/")