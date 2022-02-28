# test_appendData.py

import os, pytest, openpyxl
import pandas as pd
from openpyxl_image_loader import SheetImageLoader
from PIL import Image, ImageChops
from src.models.trading_documenter_model import TradingDocumenterModel

"""Tests whether snippet is appended to the excel file"""

@pytest.fixture
def testing_file_path():
    return os.path.abspath("tests/unit/fixtures/testing_append_snippet.xlsx")

@pytest.fixture
def testing_snippet_path():
    return os.path.abspath("tests/unit/fixtures/testing_snippet.PNG")

@pytest.fixture
def get_appended_snippet(testing_file_path, testing_snippet_path):

    data_frame = pd.read_excel(testing_file_path)
    last_row = data_frame.tail(1)

    wb = openpyxl.load_workbook(testing_file_path)
    ws = wb.worksheets[0]
    image_loader = SheetImageLoader(ws)

    cell = 'N' + str(last_row.index[0] + 2)
    appended_image = image_loader.get(cell)
    file_image = Image.open(testing_snippet_path)

    return [appended_image, file_image]

def test_if_appendData_working(testing_file_path, testing_snippet_path,  get_appended_snippet):
    """testing_snippet.PNG should match appended snippet taken from the excel file"""

    TradingDocumenterModel.appendSnippet(testing_file_path, testing_snippet_path)

    # Look up openpyxl/imageloader testing comparison
    assert ImageChops.difference(get_appended_snippet[0], get_appended_snippet[1]).getbbox() == None
    