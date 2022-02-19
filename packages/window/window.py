"""
    Import required modules.

    Password: For password generation.
    PyQt5: For the GUI.
"""

from ..password import Password
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
    The following code is for the GUI.
    """

    def setupUi(self, MainWindow) -> None:
        """
        setupUi is a method that will setup the GUI.

        Args:
            MainWindow (class): The class that will be used to create the GUI.
        """

        MainWindow.setObjectName("MainWindow")  # Set the name of the window
        MainWindow.setFixedSize(646, 443)  # Set the size of the window

        self.centralwidget = QtWidgets.QWidget(MainWindow)  # Create a central widget
        self.centralwidget.setObjectName(
            "centralwidget"
        )  # Set the name of the central widget

        self.tips_label()  # Call the tips_label method
        self.horizontal_line()  # Call the horizontal_line method
        self.password_text_area()  # Call the password_text_area method
        self.generate_button()  # Call the generate_button method
        self.strength_bar()  # Call the strength_bar method

        MainWindow.setCentralWidget(self.centralwidget)  # Set the central widget

        self.retranslateUi(MainWindow)  # Translate the GUI
        QtCore.QMetaObject.connectSlotsByName(MainWindow)  # Connect the slots

    def generate_button(self) -> None:
        """
        generate_button is a method that will create a button.
        """
        self.generate_button = QtWidgets.QPushButton(
            self.centralwidget
        )  # Create a button
        self.generate_button.setGeometry(
            QtCore.QRect(430, 290, 120, 61)
        )  # Set the geometry of the button

        font = QtGui.QFont()  # Create a font
        font.setFamily("Ubuntu")  # Set the family of the font

        self.generate_button.setFont(font)  # Set the font of the button
        self.generate_button.setAutoDefault(False)  # Set the auto default of the button
        self.generate_button.setFlat(False)  # Set the flat of the button
        self.generate_button.setObjectName(
            "generate_button"
        )  # Set the name of the button
        self.generate_button.clicked.connect(
            self.generate_password
        )  # Connect the button to the generate_password method

    def password_text_area(self) -> None:
        """
        password_text_area is a method that will create a text box.
        """
        self.password_text = QtWidgets.QLineEdit(
            self.centralwidget
        )  # Create a text box
        self.password_text.setGeometry(
            QtCore.QRect(89, 290, 331, 61)
        )  # Set the geometry of the text box

        font = QtGui.QFont()  # Create a font
        font.setFamily("Ubuntu")  # Set the family of the font

        self.password_text.setFont(font)  # Set the font of the text box
        self.password_text.setFocusPolicy(
            QtCore.Qt.ClickFocus
        )  # Set the focus policy of the text box
        self.password_text.setStyleSheet("")  # Set the style sheet of the text box
        self.password_text.setText("")  # Set the text of the text box
        self.password_text.setMaxLength(64)  # Set the maximum length of the text box
        self.password_text.setPlaceholderText(
            ""
        )  # Set the placeholder text of the text box
        self.password_text.setObjectName(
            "password_text"
        )  # Set the name of the text box
        self.password_text.textChanged.connect(self.validate_password)

    def strength_bar(self) -> None:
        """
        strength_bar is a method that will create a strength meter.
        """

        self.strength_meter = QtWidgets.QProgressBar(
            self.centralwidget
        )  # Create a strength meter
        self.strength_meter.setGeometry(
            QtCore.QRect(90, 360, 460, 34)
        )  # Set the geometry of the strength meter
        self.strength_meter.setProperty(
            "value", 0
        )  # Set the value of the strength meter
        self.strength_meter.setObjectName(
            "strength_meter"
        )  # Set the name of the strength meter

    def tips_label(self) -> None:
        """
        tips_label is a method that will create a label to display tips.
        """

        self.label = QtWidgets.QLabel(self.centralwidget)  # Create a label
        self.label.setGeometry(
            QtCore.QRect(90, 20, 460, 231)
        )  # Set the geometry of the label
        self.label.setObjectName("label")  # Set the name of the label

    def horizontal_line(self) -> None:
        """
        horizontal_line is a method that will create a horizontal line.
        """

        self.line = QtWidgets.QFrame(self.centralwidget)  # Create a line
        self.line.setGeometry(
            QtCore.QRect(90, 260, 460, 3)
        )  # Set the geometry of the line
        self.line.setFrameShape(QtWidgets.QFrame.HLine)  # Set the shape of the line
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)  # Set the shadow of the line
        self.line.setObjectName("line")  # Set the name of the line

    def retranslateUi(self, MainWindow) -> None:
        """
        retranslateUi is a method that will translate the GUI.

        Args:
            MainWindow (class): The class that will be used to create the GUI.
        """

        _translate = (
            QtCore.QCoreApplication.translate
        )  # Create a variable that will translate the GUI

        MainWindow.setWindowTitle(
            _translate(
                "Password Generator and Strength Checker",
                "Password Generator and Strength Checker",
            )
        )  # Set the title of the window

        self.generate_button.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-style:italic;">Click to generate random password.</span></p></body></html>',
            )
        )  # Set the tooltip of the button

        self.generate_button.setText(
            _translate("MainWindow", "Generate")
        )  # Set the text of the button

        self.password_text.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-style:italic;">Type your password to check strength or hit Generate for a new one.</span></p></body></html>',
            )
        )  # Set the tooltip of the text box

        self.strength_meter.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-style:italic;">Strength of the password.</span></p></body></html>',
            )
        )  # Set the tooltip of the strength meter

        self.strength_meter.setFormat(_translate("MainWindow", u"Strength %p%", None))

        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Tips for a Good Password </span></p><p>At least 8 characters.</p><p>A mixture of both uppercase and lowercase letters.</p><p>A mixture of letters and numbers.</p><p>Inclusion of at least one special character.</p></body></html>',
            )
        )  # Set the text of the label

    def generate_password(self) -> None:
        """
        generate_password is a method that will generate a random password.

        Returns:
            [str]: a string that is the generated password.
        """

        password = Password().generate()
        # Create a variable that will generate a random password

        self.password_text.setText(password)

    def validate_password(self) -> None:
        """
        validate_password is a method that will validate a password.

        Returns:
            [str]: a string that is the validated password.
        """

        strength = Password().validate(self.password_text.text())
        # Create a variable that will validate a password

        self.strength_meter.setProperty(
            "value", strength
        )  # Set the strength meter to 0
