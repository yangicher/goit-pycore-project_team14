from collections import UserDict
from datetime import datetime, timedelta
from colorama import Fore

from models.note import Note
from models.record import Record


DATE_FORMAT = "%d.%m.%Y"
DAYS_IN_WEEK = 7
WEEKEND_DAYS = [5, 6]  # Saturday and Sunday


class AddressBook(UserDict):
    """
    AddressBook is a specialized dictionary for storing and managing contact records.

    Methods:
        add_record(record: Record):
            Adds a new contact record to the address book. If the contact already exists, adds a phone number to the existing contact.

        find(name: str):
            Finds and returns a contact record by name. Returns None if the contact is not found.

        delete(name: str):
            Deletes a contact record by name. Prints a message if the contact is not found.

        get_upcoming_birthdays():
            Returns a list of contacts with upcoming birthdays within the next week. Adjusts for weekends.
    """

    def __init__(self):
        super().__init__()
        self.notes = {}

    def add_record(self, record: Record):
        """
        Adds a record to the address book. If the record's name does not exist in the address book,
        the record is added. If the record's name already exists, the phone number from the new record
        is added to the existing contact.

        Args:
            record (Record): The record to be added to the address book.

        Prints:
            str: A message indicating whether a new contact was added or an existing contact was updated.
        """
        if not self.data.get(record.name.value):
            self.data[record.name.value] = record
            print(
                f"\n{Fore.GREEN}Contact {Fore.CYAN}{record.name.value} {Fore.GREEN}added.\n"
            )
        else:
            self.data[record.name.value].add_phone(record.phones[0].value)
            print(
                f"\n{Fore.GREEN}Phone number {Fore.CYAN}{record.phones[0].value} {Fore.GREEN}added to the contact {Fore.CYAN}{record.name.value}{Fore.GREEN}.\n"
            )

    def find(self, name: str):
        """
        Find a contact by name in the address book.

        Args:
            name (str): The name of the contact to find.

        Returns:
            The contact information if found, otherwise None.
        """
        return self.data.get(name, None)

    def delete(self, name):
        """
        Deletes a contact from the address book by name.

        Parameters:
        name (str): The name of the contact to be deleted.

        Returns:
        None

        Raises:
        KeyError: If the contact with the given name is not found in the address book.
        """
        try:
            self.data.pop(name)
            print(f"\n{Fore.GREEN}Contact {Fore.CYAN}{name} {Fore.GREEN}deleted.\n")
        except KeyError:
            print(f"\n{Fore.RED}Contact {Fore.CYAN} {name} {Fore.RED}not found.\n")

    def get_upcoming_birthdays(self, days):
        """
        Get a list of upcoming birthdays within the specified number of days.

        This method checks each user's birthday and calculates if it falls within the next
        specified days from the current date. If the birthday falls on a weekend, it adjusts
        the date to the next Monday.

        Returns:
            list: A list of dictionaries, each containing the user's name and their next
                upcoming birthday in the specified date format.
        """

        if len(self.data) == 0:
            return []
        today = datetime.now().date()
        upcoming_birthdays = []

        for user in self.data.values():
            if user.birthday is not None:
                birthday_this_year = user.birthday.value.date().replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                days_until_birthday = (birthday_this_year - today).days

                if 0 <= days_until_birthday <= days:
                    if birthday_this_year.weekday() in WEEKEND_DAYS:
                        days_to_monday = 7 - birthday_this_year.weekday()
                        birthday_this_year += timedelta(days=days_to_monday)

                    upcoming_birthdays.append(
                        {
                            "name": user.name.value,
                            "next_upcoming_birthday": birthday_this_year.strftime(
                                DATE_FORMAT
                            ),
                        }
                    )

        return upcoming_birthdays

    def add_note(self, title: str, content: str):
        """
        Adds a note with the given title and content to the address book.

        Args:
            title (str): The title of the note.
            content (str): The content of the note.

        Raises:
            ValueError: If a note with the given title already exists.

        Prints:
            A success message indicating that the note was added.
        """

        if title in self.notes:
            raise ValueError(
                f"\n{Fore.GREEN}Note with title {Fore.CYAN}{title} {Fore.GREEN}already exists.\n"
            )
        self.notes[title] = Note(title, content)
        print(
            f"\n{Fore.GREEN}Note {Fore.CYAN}{title} {Fore.GREEN}added successfully.\n"
        )

    def delete_note_by_title(self, title: str):
        """
        Deletes a note by its title.

        Args:
            title (str): The title of the note to be deleted.

        Raises:
            KeyError: If the note with the specified title is not found.

        Prints:
            Success message if the note is deleted successfully.
        """

        if title not in self.notes:
            raise KeyError(
                f"\n{Fore.RED}Note with title {Fore.CYAN}{title}{Fore.RED} not found.\n"
            )

        del self.notes[title]
        print(
            f"\n{Fore.GREEN}Note {Fore.CYAN}{title}{Fore.GREEN} deleted successfully.\n"
        )

    def edit_note(self, title: str, new_content: str):
        """
        Edit the content of an existing note.

        Args:
            title (str): The title of the note to be edited.
            new_content (str): The new content to replace the existing content of the note.

        Raises:
            KeyError: If a note with the specified title does not exist.

        Prints:
            A success message indicating that the note has been updated.
        """

        if title not in self.notes:
            raise KeyError(
                f"\n{Fore.RED}Note with title {Fore.CYAN}{title}{Fore.RED} not found.\n"
            )

        self.notes[title].value = new_content
        print(
            f"\n{Fore.GREEN}Note {Fore.CYAN}{title}{Fore.GREEN} updated successfully.\n"
        )

    def find_notes(self, query: str):
        """
        Searches for notes that contain the given query in their title or value.

        Args:
            query (str): The search string to look for in the notes.

        Returns:
            dict or str: A dictionary of found notes where the keys are the note identifiers
                         and the values are the note objects. If no notes are found, returns
                         a string message indicating no matches.
        """
        
        found_notes = {
            key: note
            for key, note in self.notes.items()
            if query.lower() in note.title.lower()
            or query.lower() in note.value.lower()
        }

        return found_notes

    def find_note_by_title(self, note_title: str) -> Note | None:
        """
        Find a note by its title.

        Args:
            note_title (str): The title of the note to find.

        Returns:
            Note | None: The note object if found, otherwise None.
        """

        for title, note in self.notes.items():
            if title.lower() == note_title.lower():
                return note
        return None

    def find_notes_by_tag(self, tag: str) -> list[Note]:
        """
        Find notes by a specific tag.
        Args:
            tag (str): The tag to search for in the notes.
        Returns:
            list[Note]: A list of notes that contain the specified tag.
        """

        notes = {
            key: note for key, note in self.notes.items() if note.is_tag_exists(tag)
        }
        return notes

    def get_contacts(self):
        """
        Retrieve all contacts from the address book.

        Returns:
            dict: A dictionary containing all contacts.
        """

        return self.data

    def get_notes(self):
        """
        Retrieve the notes associated with the address book.
        Returns:
            list: A list of notes.
        """

        return self.notes
