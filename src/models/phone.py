import re

from models import Field

PATTERN = r"^\d{10}$"


class Phone(Field):
    """
    A class used to represent a Phone number.

    Attributes
    ----------
    value : str
        The phone number value.

    Methods
    -------
    __init__(value)
        Initializes the Phone object with a given value. If the value matches the
        specified pattern, it is assigned to the value attribute. Otherwise, the
        value is set to None and an error message is printed.
    """

    def __init__(self, value):
        super().__init__(value)
        if re.match(PATTERN, value):
            self.value = value
        else:
            self.value = None
            print("Invalid phone number. Please enter a 10-digit number.")
