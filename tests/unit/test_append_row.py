# test_appendData.py

import os, shutil
from datetime import datetime

import pandas as pd
from pandas.testing import assert_frame_equal
from src.models.trading_documenter_model import TradingDocumenterModel

"""Tests whether row data is appended to the excel file"""

model = TradingDocumenterModel()

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

def get_pre_path():
    return "tests/unit/fixtures/"

def get_Abs_Path():
    pre_path = get_pre_path()
    folder_and_file_name = datetime.today().strftime("%m-%d-%Y")

    model.directory = pre_path + folder_and_file_name + "/"
    model.AbsPath = os.path.abspath(pre_path + folder_and_file_name + "/" + folder_and_file_name + ".xlsx")

    return model.AbsPath

def get_appended_data():
    data_frame = pd.read_excel(model.AbsPath, index_col=None)
    last_row = data_frame.tail(1)

    return last_row

def test_if_appendData_working():
    """get_sample_dict should match appended data taken from the excel file"""
    
    get_Abs_Path()
    
    model._create_excel_file_name()

    model.appendDataToExcel(get_sample_dict())

    assert assert_frame_equal(get_appended_data(), pd.DataFrame.from_dict([get_sample_dict()])) == None

    shutil.rmtree(get_pre_path() + datetime.today().strftime("%m-%d-%Y") + "/")