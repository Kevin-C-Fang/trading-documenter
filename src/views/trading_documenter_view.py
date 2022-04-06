# Filename: trading_documenter_view.py

"""Prvoides TradingDocumenterView, class for implementing GUI/View of desktop application

TradingDocumenterView implements the front-end/UI of the application using layouts and widgets from QWidgets.
"""

# Import PyQt5 and the required widgets from PyQt5.QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout,QHBoxLayout, QLabel, QGroupBox, QLineEdit, QPlainTextEdit,
                             QMainWindow, QMessageBox, QPushButton, QWidget, QCheckBox)

class TradingDocumenterView(QMainWindow):
    """Class that implements the view for the Model-View-Controller(MVC) design pattern."""

    def __init__(self) -> None:
        """View Initializer"""
        super().__init__()

        # Set properties such as window name, icon, size, and placement when executed
        self.setWindowTitle("Trading Documenter | Day Trading Documenter")
        self.setWindowIcon(QIcon('imgs/icon.png'))
        self.setFixedSize(1120, 640)
        self.move(400, 200)

        # Set general/main vertical layout through QWidget
        self._general_vertical_layout = QVBoxLayout()
        _central_widget = QWidget(self)
        _central_widget.setLayout(self._general_vertical_layout)
        self.setCentralWidget(_central_widget)
        
        # Create title heading, options, notes, and buttons
        self._create_title_heading()
        self._add_options_notes_snippet()
        self._create_enter_and_clear_buttons()

    def _create_title_heading(self) -> None:
        """Create title heading, align center, and adds to _general_vertical_layout"""

        msg = QLabel("<h1>Trading Documenter</h1>")
        msg.setAlignment(Qt.AlignCenter)
        self._general_vertical_layout.addWidget(msg)

    def _add_options_notes_snippet(self) -> None:
        "Creates horizontal layout with inner vertical layout for options/notes and snippet on the horizontal layout which is passed to functions for implementation of those features"

        options_and_notes_horizontal_layout = QHBoxLayout()
        vbox = QVBoxLayout()
        options_and_notes_horizontal_layout.setContentsMargins(60, 0, 60, 0)

        self._general_vertical_layout.addLayout(options_and_notes_horizontal_layout)
        vbox = QVBoxLayout()
        options_and_notes_horizontal_layout.addLayout(vbox)

        self._create_options(vbox)
        self._create_notes(vbox)
        self._create_snippet(options_and_notes_horizontal_layout)

        

    # Change func name?
    def _set_QGroupBox_properties(self, title, options_and_notes_layout) -> QVBoxLayout:
        "TBD"
        # Name, doc, parameters, and pub/priv

        group_box = QGroupBox(title)
        group_box.setStyleSheet("QGroupBox { font-weight: bold; font-size: 16px; }"
                                "QCheckBox { font-weight: bold; font-size: 12px; }"
                                "QLineEdit { font-weight: bold; font-size: 12px; }"
                                "QPushButton { font-weight: bold; font-size: 12px; }"
                                "QPlainTextEdit { font-weight: bold; font-size: 12px; }")
        options_and_notes_layout.addWidget(group_box)

        vLayout = QVBoxLayout()
        group_box.setLayout(vLayout)
        
        return vLayout

    def _create_options(self, options_and_notes_layout) -> None:
        "TBD"

        vLayout = self._set_QGroupBox_properties("Options", options_and_notes_layout)

        self.options = [QCheckBox("Win"), QCheckBox("Lose"), QCheckBox("Patient/Not Emotional"), QCheckBox("ATR"), 
                        QCheckBox("Price Action"), QCheckBox("Time Frames"), QCheckBox("Cumulative Delta"), 
                        QCheckBox("Trend Lines"), QCheckBox("SMA"), QCheckBox("Volume Profile")]

        self.options.append(QLineEdit())
        self.options[-1].setPlaceholderText("Risk:Reward")
        self.options[-1].setFixedWidth(100)

        self.options.append(QPushButton("Snippet"))
        self.options[-1].setFixedWidth(100)

        for option in self.options:
            vLayout.addWidget(option)

    def _create_notes(self, options_and_notes_layout) -> None:
        """TBD"""
        # Name, doc, parameters, and pub/priv
        
        vLayout = self._set_QGroupBox_properties("Notes", options_and_notes_layout)
        textBox = QPlainTextEdit()
        vLayout.addWidget(textBox)

    def _create_snippet(self, options_and_notes_layout) -> None:
        """TBD"""
        # Name, doc, parameters, and pub/priv
        vLayout = self._set_QGroupBox_properties("Snippet", options_and_notes_layout)

        label = QLabel("Snippet")
        pixmap = QPixmap("imgs/filler.PNG")
        label.setPixmap(pixmap)
        
        vLayout.addWidget(label)

    def _create_enter_and_clear_buttons(self) -> None:
        """Create enter/clear buttons with properties added to a horizontal layout which is added on to the _general_vertical_layout"""

        # Creation and addition of QHBoxLayout to _general_vertical_layout
        horizontal_layout = QHBoxLayout()
        self._general_vertical_layout.addLayout(horizontal_layout)

        self.buttons = [QPushButton("Enter"), QPushButton("Clear")]

        # Set button properties and add buttons to horizontal layout
        for button in self.buttons:
            button.setFixedSize(60, 35)
            horizontal_layout.addWidget(button)

    def msg_Popup_Box(self, message: str) -> None:
        """Creates a message box with text using the parameter message and pops up in the middle of the window
        
        message: String to be shown on the message box
        """

        alert = QMessageBox()
        alert.setText(message)
        alert.exec_()