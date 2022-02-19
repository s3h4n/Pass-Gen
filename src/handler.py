"""
    Import required modules.

    Ui_MainWindow: The main window of the application.
    QtWidgets: The QtWidgets module.
    sys: The sys module.
"""

from ..packages import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class Handler:
    """
    End handler.
    """

    def __init__(self) -> None:
        """
        __init__ is the constructor for the class.
        """
        pass

    def handler(self) -> None:
        """
        handler is the method that will handle the request.

        Args:
            None

        Returns:
            None: None.
        """

        # Create an instance of the application window and run it
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()

        # Create an instance of the UI class
        ui = Ui_MainWindow()

        # Call the UI's setupUi method
        ui.setupUi(MainWindow)

        # Show the application window
        MainWindow.show()

        # Run the application
        sys.exit(app.exec_())
