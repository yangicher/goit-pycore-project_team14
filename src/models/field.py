class Field:
    """
    A class used to represent a Field.

    Attributes
    ----------
    value : any
        The value stored in the field.

    Methods
    -------
    __str__()
        Returns the string representation of the field's value.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)