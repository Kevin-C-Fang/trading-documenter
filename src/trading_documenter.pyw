#!/usr/bin/env python

# Filename: trading_documenter.pyw

"""Trading documenter is a desktop GUI that allows the user to record trades they have made."""

#Import sys for clean closing of application memory
import sys

# Import QApplication to create instance of application GUI
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# Import MVC file to run GUI UI/UX
from views.trading_documenter_view import TradingDocumenterView
from controllers.trading_documenter_controller import TradingDocumenterController
from models.trading_documenter_model import TradingDocumenterModel


def main():
    """Main/Runner Function"""
    app = QApplication([])

    window = TradingDocumenterView()
    window.show()

    model = TradingDocumenterModel()
    TradingDocumenterController(model_Obj=model, view_Obj=window)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()