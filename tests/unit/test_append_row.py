# test_appendData.py

import os, pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.models.trading_documenter_model import TradingDocumenterModel

"""Tests whether row data is appended to the excel file"""

@pytest.fixture
def sample_row_data():
    return pd.DataFrame({
        "Win/Loss": "Win",
        "Risk:Reward": "1:1.25",
        "Patient": "Yes",
        "Not Emotional": "Yes",
        "ATR": "Yes",
        "Price Action": "Yes",
        "Time Frames": "Yes",
        "Cumulative Delta": "No",
        "Trend Lines": "No",
        "SMA": "No",
        "Volume Profile": "No",
        "Notes": """No""",
        "Snippet": None
    }, index=[0])

@pytest.fixture
def testing_file_path():
    return os.path.abspath("tests/unit/fixtures/testing_append_row.xlsx")

@pytest.fixture
def get_appended_data(testing_file_path):
    data_frame = pd.read_excel(testing_file_path())
    last_row = data_frame.tail(1)

    return last_row

def test_if_appendData_working(sample_row_data, testing_file_path, get_appended_data):
    """sample_row_data should match appended data taken from the excel file"""
    
    TradingDocumenterModel.appendData(testing_file_path, sample_row_data)

    assert assert_frame_equal(get_appended_data(), sample_row_data, check_dtype=False) == None
    