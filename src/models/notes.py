from models.field import Field

class Note(Field):
    """
    A class to represent a note with a title and content.

    Attributes:
        title (str): The title of the note
        value (str): The content of the note
    """

    def __init__(self, title: str, content: str):
        self.title = title
        super().__init__(content)

    def __str__(self):
        return f"{self.title}: {self.value}"