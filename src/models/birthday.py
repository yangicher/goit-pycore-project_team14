from datetime import datetime

from .field import Field


class Birthday(Field):
    """ The Birthday class represents a date of birth and extends the Field class.

    Attributes:
        value (datetime): The date of birth as a datetime object.

    Methods:
        __init__(value):
            Initializes the Birthday object with a date string in the format DD.MM.YYYY.
            Raises a ValueError if the date string is not in the correct format.
        
        __str__():
            Returns the date of birth as a string in the format DD.MM.YYYY.
    """
    def __init__(self, value):
        super().__init__(value)
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y")
            self.value = date_obj
        except ValueError as exc:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from exc

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
