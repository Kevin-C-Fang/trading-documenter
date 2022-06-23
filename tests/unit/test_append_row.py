# test_appendData.py

import datetime
import os, pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.models.trading_documenter_model import TradingDocumenterModel

"""Tests whether row data is appended to the excel file"""

@pytest.fixture
def get_sample_dict():
    return {"Win": "✓",
            "Lose": "✗",
            "Patient": "✗",
            "ATR": "✓",
            "Price Action": "✗",
            "Time Frames": "✓",
            "Trend Lines": "✗",
            "SMA": "✓",
            "Volume Profile": "✓",
            "Risk:Reward": "1:1.25",
            "Notes": """Testing""",
            "Path": "data/6-20-2022/"
            }


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

@pytest.fixture
def get_appended_data():
    data_frame = pd.read_excel(TradingDocumenterModel.AbsPath)
    last_row = data_frame.tail(1)

    return last_row

def test_if_appendData_working(sample_row_data, testing_file_path, get_appended_data):
    """get_sample_dict should match appended data taken from the excel file"""
    
    TradingDocumenterModel.appendDataToExcel(get_sample_dict)

    assert assert_frame_equal(get_appended_data, get_sample_dict) == None