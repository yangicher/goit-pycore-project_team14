from models.field import Field

class Address(Field):
    """
    A class used to represent a physical address.

    Attributes
    ----------
    value : str
        The address value.

    Methods
    -------
    __init__(value)
        Initializes the Address object with basic validation.
    """

    def __init__(self, value):
        if len(value.strip()) < 1:
            raise ValueError("Address cannot be empty")
        super().__init__(value)