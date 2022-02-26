# test_create_excel_column_headers.py

import os, pytest
import pandas as pd

from src.models.trading_documenter_model import TradingDocumenterModel

"""Tests the creation of the excel file headers"""

@pytest.fixture
def sample_row_data():
    return ["Unnamed: 0", "Win/Loss", "Risk:Reward", "Patient", "Not Emotional", "ATR", "Price Action",
                 "Time Frames", "Cumulative Delta", "Trend Lines", "SMA", "Volume Profile", "Notes", "Snippet"]

@pytest.fixture
def testing_file_path():
    return os.path.abspath("tests/unit/fixtures/testing_headers.xlsx")

@pytest.fixture
def created_file_headers():
    data_frame = pd.read_excel(testing_file_path)

    return data_frame.columns.tolist()

def test_if_create_excel_column_headers_working():
    """ sample_row_data headers should match headers taken from the excel file"""
    TradingDocumenterModel._create_excel_column_headers(testing_file_path())

    assert created_file_headers() == sample_row_data()
    assert not created_file_headers() == []