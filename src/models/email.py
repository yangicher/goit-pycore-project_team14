import re
from src.models.field import Field

class Email(Field):
    """
    A class used to represent an Email field.

    Attributes:
        value (str): The email value

    Methods:
        __init__(value):
            Initializes the Email object with validation
    """
    def __init__(self, value):
        # Email validation pattern
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError("Invalid email format")
        super().__init__(value)