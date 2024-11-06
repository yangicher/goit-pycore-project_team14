import re
from models.field import Field

class Email(Field):
    """
    A class used to represent an Email address.

    Attributes
    ----------
    value : str
        The email address value.

    Methods
    -------
    __init__(value)
        Initializes the Email object with validation.
    """

    def __init__(self, value):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"Invalid email format: {value}. Please enter a valid email address.")
        super().__init__(value)