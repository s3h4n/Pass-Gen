""" 
    Import required modules

    random: For random number generation
"""
import random


class Password:
    """
    This will be used to generate a password that is not easily guessable.
    """

    def __init__(self) -> None:
        """
        __init__ is the constructor for the Password class.
        """

        self.atoz_lower = "abcdefghijklmnopqrstuvwxyz"  # Lowercase alphabet
        self.atoz_upper = "".join(self.atoz_lower).upper()  # Uppercase alphabet
        self.int_numbers = "1234567890"  # Numbers
        self.special_chars = "`~!@#$%^&*()-_=+{[]}\|;:,.?/"  # Special characters

        self.char_set = list(
            self.atoz_lower + self.atoz_upper + self.int_numbers + self.special_chars
        )

    def generate(self, length: int = 12) -> str:
        """
        Generate is the method that will generate a password.

        Args:
            length (int, optional): Length of the password. Defaults to 12.

        Returns:
            str: The generated password.
        """

        random.shuffle(self.char_set)

        password = "".join(random.sample(self.char_set, length))[0:length]

        return password

    def validate(self, password: str) -> bool:
        """
        validate is the method that will validate a password.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if the password is valid, False if not.
        """

        score = 100

        # Check if the password is at least 8 characters long
        if len(password) < 8:
            score -= 20

        # Check if the password contains at least one lowercase letter
        if not any(char.islower() for char in password):
            score -= 20

        # Check if the password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            score -= 20

        # Check if the password contains at least one number
        if not any(char.isdigit() for char in password):
            score -= 20

        # Check if the password contains at least one special character
        if not any(char in self.special_chars for char in password):
            score -= 20

        return score
