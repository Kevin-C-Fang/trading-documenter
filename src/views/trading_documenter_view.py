# Filename: trading_documenter_view.py

"""Provides TradingDocumenterView, class for implementing GUI/View of desktop application

TradingDocumenterView implements the front-end/UI of the application using layouts and widgets from QWidgets.
"""

# Import ctypes to tell windows this is my registered application
from asyncio.windows_events import NULL
import ctypes
import os
from datetime import datetime
from types import NoneType

# Import ImageGrab from PIL for getting contents of clipboard
from PIL import ImageGrab

# Import PyQt5 and the required widgets from PyQt5.QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout,QHBoxLayout, QLabel, QGroupBox, QLineEdit, QPlainTextEdit,
                             QMainWindow, QMessageBox, QPushButton, QWidget, QCheckBox)

class TradingDocumenterView(QMainWindow):
    """Class that implements the view for the Model-View-Controller(MVC) design pattern.
    
    :param QVBoxLayout _general_vertical_layout: Vertical layout that holds the controls
    :param list[QPushButton] EnterAndClearButtons: List of enter and clear buttons
    :param list[Union[[QCheckBox, QLineEdit, QPushButton]] Options: List of widgets for options
    :param QPlainTextEdit Notes: Widget for holding notes
    :param QLabel _screenshot_label: Label that holds the screenshot/QPixMap
    :param str ScreenshotPath: Absolute path of screenshot 
    """

    ScreenshotPath = ""

    def __init__(self) -> None:
        """View Initializer"""
        super().__init__()

        # Change Taskbar icon
        my_app_id = 'kevincfang.trading_documenter' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

        # Set properties such as window name, icon, size, and placement when executed
        self.setWindowTitle("Trading Documenter | Day Trading Documenter")
        self.setWindowIcon(QIcon('imgs/application/icon.png'))
        self.setFixedSize(1120, 640)
        self.move(400, 200)

        # Create general verticle layout and set for widget/screen
        self._general_vertical_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self._general_vertical_layout)
        self.setCentralWidget(central_widget)
        
        # Create title heading, options, notes, and buttons
        self._create_title_heading()
        self._add_options_notes_screenshot()
        self._create_enter_and_clear_buttons()

    def _create_title_heading(self) -> None:
        """Create title heading, align center, and add to _general_vertical_layout"""

        title = QLabel("<h1>Trading Documenter</h1>")
        title.setAlignment(Qt.AlignCenter)
        self._general_vertical_layout.addWidget(title)

    def _add_options_notes_screenshot(self) -> None:
        "Creates layouts to be added to _general_vertical_layout and calls create functions for each groupbox section"

        # Create layouts and add vertical to horizontal then horizontal onto _general_vertical_layout
        options_notes_screenshot_horizontal_layout = QHBoxLayout()
        options_notes_screenshot_horizontal_layout.setContentsMargins(80, 0, 80, 0)
        options_notes_vertical_layout = QVBoxLayout()
        options_notes_screenshot_horizontal_layout.addLayout(options_notes_vertical_layout)

        self._general_vertical_layout.addLayout(options_notes_screenshot_horizontal_layout)

        self._create_options(options_notes_vertical_layout)
        self._create_notes(options_notes_vertical_layout)
        self._create_screenshot(options_notes_screenshot_horizontal_layout)

    def _create_options(self, options_notes_vertical_layout) -> None:
        """Creates options to be added to internal group box layout
        
        :param QVBoxLayout options_notes_vertical_layout: Layout to add groupbox to
        """

        options_group_box_Layout = self._create_groupbox("Options", options_notes_vertical_layout)

        # Create options and add to group_box_Layout
        self.Options = [QCheckBox("Win"), QCheckBox("Lose"), QCheckBox("Patient"), QCheckBox("ATR"), 
                        QCheckBox("Price Action"), QCheckBox("Time Frames"), QCheckBox("Trend Lines"), QCheckBox("SMA"), QCheckBox("Volume Profile")]

        self.Options.append(QLineEdit())
        self.Options[-1].setPlaceholderText("Risk:Reward")
        self.Options[-1].setFixedWidth(110)

        self.Options.append(QPushButton("Copy Clipboard"))
        self.Options[-1].setFixedWidth(110)

        for option in self.Options:
            options_group_box_Layout.addWidget(option)

    def _create_notes(self, options_notes_vertical_layout) -> None:
        """Creates notes to be added to internal group box layout
        
        :param QVBoxLayout options_notes_vertical_layout: Layout to add groupbox to
        """
        
        notes_group_box_Layout = self._create_groupbox("Notes", options_notes_vertical_layout)
        self.Notes = QPlainTextEdit("""Pro:\n\nCon:\n""")
        notes_group_box_Layout.addWidget(self.Notes)

    def _create_screenshot(self, options_notes_screenshot_horizontal_layout) -> None:
        """Creates screenshot picture to be added to internal group box layout
        
        :param QHBoxLayout options_notes_screenshot_horizontal_layout: Layout to add groupbox to
        """

        screenshot_group_box_layout = self._create_groupbox("Screenshot", options_notes_screenshot_horizontal_layout)

        # Create label and attach Pixmap
        self._screenshot_label = QLabel()
        self._screenshot_label.setPixmap(QPixmap("imgs/application/filler.PNG"))
        
        screenshot_group_box_layout.addWidget(self._screenshot_label)

    def _create_groupbox(self, title, layout) -> QVBoxLayout:
        """Creates group box with internal layout to be returned for adding components
        
        :param Union[QVBoxLayout, QHBoxLayout] layout: Layout to add group box to
        """

        group_box = QGroupBox(title)
        group_box.setStyleSheet("QGroupBox { font-weight: bold; font-size: 16px; }"
                                "QCheckBox { font-weight: bold; font-size: 12px; }"
                                "QLineEdit { font-weight: bold; font-size: 12px; }"
                                "QPushButton { font-weight: bold; font-size: 12px; }"
                                "QPlainTextEdit { font-weight: bold; font-size: 12px; }")
        layout.addWidget(group_box)

        group_box_Layout = QVBoxLayout()
        group_box.setLayout(group_box_Layout)
        
        return group_box_Layout

    def _create_enter_and_clear_buttons(self) -> None:
        """Create enter/clear buttons with properties to a horizontal layout which is added on to the _general_vertical_layout"""

        # Created and added horizontal layout to _general_vertical_layout
        horizontal_layout = QHBoxLayout()
        self._general_vertical_layout.addLayout(horizontal_layout)

        self.EnterAndClearButtons = [QPushButton("Enter"), QPushButton("Clear")]

        # Set button properties and add buttons to horizontal layout
        for button in self.EnterAndClearButtons:
            button.setFixedSize(60, 35)
            horizontal_layout.addWidget(button)

    def clearAllValues(self) -> None:
        """Clears all values in QWidgets/Controls"""

        for option in self.Options:
            data_type = type(option)
            if data_type == QCheckBox:
                option.setChecked(False)
            elif data_type == QLineEdit:
                option.clear()

        self.Notes.clear()
        self._screenshot_label.setPixmap(QPixmap("imgs/application/filler.PNG"))

    def takeScreenshot(self) -> None:
        """Saves screenshot of trade and shows in preview"""
        
        # Create absolute path and directory if needed
        today = datetime.today().strftime("%m-%d-%Y")
        specified_time_and_date = datetime.now().strftime("%m-%d-%Y, %H-%M-%S")
        abs_path = os.path.abspath("data/" + today + "/" + specified_time_and_date + ".PNG")  

        # Create abs path for intended directory to check if it exists
        check_path = os.path.abspath("data/" + today)
        if not os.path.exists(check_path):
            os.makedirs(check_path)

        # Grab image from clipboard 
        clipboard_image = ImageGrab.grabclipboard()

        # If result is not an image then show message box and return
        if(type(clipboard_image) == NoneType):
            self.createMessageBox("Take a snippet by holding Windows + Shift + S")
            return

        # Save image and path to be passed to modeling
        clipboard_image.save(abs_path)
        self.ScreenshotPath = abs_path

        self._screenshot_label.setPixmap(QPixmap(abs_path).scaled(650, 450, aspectRatioMode=0, transformMode=1))

    def createMessageBox(self, message: str) -> None:
        """Creates a message box with text using the parameter message and displays in the middle of the application
        
        :param str message: message to be shown on the message box
        """

        message_Box = QMessageBox()
        message_Box.setWindowIcon((QIcon('imgs/application/icon.png')))
        message_Box.setWindowTitle("Error: Follow steps below to resolve")
        message_Box.setText(message)
        message_Box.exec_()