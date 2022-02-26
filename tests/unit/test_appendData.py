# test_appendData.py

import os, pytest
import pandas as pd
from src.models.trading_documenter_model import TradingDocumenterModel

"""Tests whether data is appended to the excel file"""

@pytest.fixture
def sample_row_data():
    return {
            "Unnamed: 0": 0,
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
            "Snippet": "No" # Needs to be fleshed out
    }

@pytest.fixture
def testing_file_path():
    return os.path.abspath("tests/unit/fixtures/testing_append.xlsx")

@pytest.fixture
def get_appended_data():
    data_frame = pd.read_excel(testing_file_path())
    last_row = data_frame.tail(1).values.tolist()[0]

    return last_row

def test_if_appendData_working():
    """sample_row_data should match appended data taken from the excel file"""
    TradingDocumenterModel._create_excel_column_headers(testing_file_path())
    TradingDocumenterModel.appendData(testing_file_path(), sample_row_data)

    assert get_appended_data() == sample_row_data()
    assert not get_appended_data() == []
    