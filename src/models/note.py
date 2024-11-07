from datetime import datetime
from models.field import Field
from models import Tag, TagDuplicateError, TagNotFound


class Note(Field):
    """
    A class used to represent a Note.

    Attributes:
        title (str): The title of the note.
        value (str): The content of the note.
        creation_date (datetime): The date and time when the note was created.

    Methods:
        change_title(new_title):
        change_content(new_content):
        __str__():
            Returns a string representation of the note.
    """

    def __init__(self, title, note):
        super().__init__(note)
        self.title: str = title
        self.value = note
        self.creation_date = datetime.now()
        self.tags: list[Tag] = []

    def change_title(self, new_title):
        """
        Changes the title of the note.

        Parameters:
        new_title (str): The new title for the note.

        Returns:
        None
        """
        self.title = new_title

    def change_content(self, new_content):
        """
        Changes the content of the note.

        Parameters:
        new_content (str): The new content for the note.

        Returns:
        None
        """
        self.value = new_content

    def add_tag(self, new_tag: str) -> None:
        for tag in self.tags:
            if tag.value == new_tag:
                raise TagDuplicateError()
        self.tags.append(tag)

    def remove_tag(self, tag_to_remove: str):
        if tag_to_remove not in self.tags:
            raise TagNotFound(f'Tag {tag_to_remove} is not linked to selected note.')
        self.tags = [tag for tag in self.tags if tag != tag_to_remove]

    def __str__(self):
        formatted_date = self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.title.upper()} created at {formatted_date}\n\n{self.value}"
