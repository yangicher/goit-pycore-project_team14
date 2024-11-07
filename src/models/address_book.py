from collections import UserDict
from datetime import datetime, timedelta

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
            print(f"Contact {record.name.value} added.")
        else:
            self.data[record.name.value].add_phone(record.phones[0].value)
            print(
                f"Phone number {record.phones[0].value} add to the contact {record.name.value}."
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
        except KeyError:
            print(f"Contact {name} not found.")

    def get_upcoming_birthdays(self, days):
        """
        Get a list of upcoming birthdays within the next week.

        This method checks each user's birthday and calculates if it falls within the next
        seven days from the current date. If the birthday falls on a weekend, it adjusts
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
            if(user.birthday != None):
                birthday_this_year = user.birthday.value.date().replace(year=today.year)
                days_until_birthday = (birthday_this_year - today).days

                if 0 <= days_until_birthday <= days:
                    if birthday_this_year.weekday() in WEEKEND_DAYS:
                        birthday_this_year += timedelta(
                            days=(days - birthday_this_year.weekday())
                        )

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
        """Add a new note to the address book."""
        if title in self.notes:
            raise ValueError(f"Note with title '{title}' already exists")
        self.notes[title] = Note(title, content)
        print(f"Note '{title}' added successfully")

    def show_notes(self):
        """Show all notes in the address book."""
        if not self.notes:
            print("No notes found")
            return

        for note in self.notes.values():
            print(note)

    def delete_note_by_title(self, title: str):
        """Delete a note by its title."""
        if title not in self.notes:
            raise ValueError(f"Note with title '{title}' not found")

        del self.notes[title]
        print(f"Note '{title}' deleted successfully")

    def edit_note(self, title: str, new_content: str):
        """Edit the content of an existing note."""
        if title not in self.notes:
            raise ValueError(f"Note with title '{title}' not found")

        self.notes[title].value = new_content  # Обновляем значение value, а не content
        print(f"Note '{title}' updated successfully")

    def find_notes(self, query: str):
        """Search notes by title or content."""
        found_notes = []
        for note in self.notes.values():
            if query.lower() in note.title.lower() or query.lower() in note.value.lower():
                found_notes.append(note)

        if not found_notes:
            print(f"No notes found matching '{query}'")
        else:
            for note in found_notes:
                print(note)
    
    def find_note_by_title(self, note_title: str) -> Note | None:
        """
        Get single note by title
        """
        for title, note in self.notes.items():
            if title.lower() == note_title.lower():
                return note
        return None