from datetime import datetime
from models.field import Field
from models.tag import Tag, TagDuplicateError, TagNotFound, auto_add_hashtag


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
        new_tag = auto_add_hashtag(new_tag)
        for tag in self.tags:
            print(f'{tag.value} ||| {new_tag}')
            if tag.value == new_tag:
                raise TagDuplicateError()
        self.tags.append(Tag(new_tag))

    def remove_tag(self, tag_to_remove: str) -> None:
        tag_to_remove = auto_add_hashtag(tag_to_remove)
        if tag_to_remove not in [tag.value for tag in self.tags]:
            raise TagNotFound()
        self.tags = [tag for tag in self.tags if tag.value != tag_to_remove]

    def __get_tags_str(self):
        result_str = '\nTags:'
        for tag in self.tags:
            result_str += f'\n{tag.value}'
        return result_str

    def __str__(self):
        formatted_date = self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.title.upper()} created at {formatted_date}\n\n{self.value}{self.__get_tags_str()}"
