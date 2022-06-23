# test_create_excel_file_name.py

import os
from datetime import datetime

import pytest
from src.models.trading_documenter_model import TradingDocumenterModel


"""Tests the creation of the excel file name based on the current date"""

@pytest.fixture
def get_pre_path():
    return "tests/unit/fixtures/"

@pytest.fixture
def get_Abs_Path():
    pre_path = get_pre_path()
    folder_and_file_name = datetime.today().strftime("%m-%d-%Y")

    TradingDocumenterModel.AbsPath = os.path.abspath(pre_path + folder_and_file_name + "/" + folder_and_file_name + ".xlsx")

    yield TradingDocumenterModel.AbsPath

    os.removedirs(pre_path + folder_and_file_name + "/")

def test_if_create_excel_file_name_working():
    """_create_excel_file_name should match current date file name"""

    TradingDocumenterModel._create_excel_file_name()

    assert os.path.exists(get_Abs_Path()) == True