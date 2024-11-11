from prompt_toolkit import HTML, PromptSession, print_formatted_text, prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from colorama import Fore

from constants.constants import COMMAND_NAMES, COMMANDS
from decorators.input_error import input_error
from helpers.data import load_data, save_data
from helpers.os import clear_console
from helpers.table_view import (
    get_birthday_table,
    get_birthdays_table,
    get_contacts_table,
    get_notes_table,
    get_phone_table,
)
from models.address_book import AddressBook
from models.record import Record
from models.note import Note

commands_completer = WordCompleter(COMMAND_NAMES.keys())
names_completer = WordCompleter([])
notes_completer = WordCompleter([])
tags_completer = WordCompleter([])

# Define the style for the welcome message
style = Style.from_dict({"welcome": "bold fg:green", "command": "fg:yellow"})

# Define the welcome message
welcome_message = HTML(
    """
<welcome>Welcome to the Address Book Assistant!</welcome>
<command>Type 'help' to see the list of available commands.</command>
"""
)


def wrapped_prompt(name: str, completer=None):
    value = prompt(HTML(f"<b>{name}</b>"), completer=completer)
    if not value:
        raise ValueError
    return value


def update_notes_completer(book: AddressBook):
    notes_completer.words = book.notes.keys()


def update_names_completer(book: AddressBook):
    names_completer.words = book.data.keys()


def update_tags_completer(book: AddressBook):
    unique_tags = {tag.value for note in book.notes.values() for tag in note.tags}
    tags_completer.words = list(unique_tags)


@input_error(COMMAND_NAMES["add_contact"])
def add_contact(book: AddressBook):
    """
    Adds a new contact to the given address book.

    Prompts the user to enter a name and a phone number, creates a new record with the provided information,
    and adds it to the address book. Also updates the names completer with the new contact.

    Args:
        book (AddressBook): The address book to which the new contact will be added.
    """

    name = wrapped_prompt("Enter name: ")
    phone = wrapped_prompt("Enter phone (10 digits): ")
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    update_names_completer(book)


@input_error(COMMAND_NAMES["add_address"])
def add_address(book: AddressBook):
    """
    Prompts the user to enter a name and an address, then adds the address to the corresponding record in the address book.

    Args:
        book (AddressBook): The address book where the contact records are stored.

    Returns:
        None

    Raises:
        None

    Notes:
        If the contact with the given name is not found in the address book, a message is printed indicating that the contact was not found.
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name} {Fore.RED}not found.\n")
        return
    address = wrapped_prompt("Enter address: ")
    record.add_address(address)


@input_error(COMMAND_NAMES["add_birthday"])
def add_birthday(book: AddressBook):
    """
    Add a birthday to a contact in the address book.

    Args:
        args (tuple): A tuple containing the name of the contact (str) and the birthday (str).
        book (AddressBook): The address book where the contact is stored.

    Returns:
        None

    Prints:
        A message indicating whether the birthday was added or if the contact was not found.
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)

    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name} {Fore.RED}not found.\n")

    birthday = wrapped_prompt("Enter birthday (DD.MM.YYYY): ")
    record.add_birthday(birthday)
    print(
        f"\n{Fore.GREEN}Birthday {Fore.CYAN}{birthday} {Fore.GREEN}added to {Fore.CYAN}{name}{Fore.GREEN}.\n"
    )


@input_error(COMMAND_NAMES["add_email"])
def add_email(book: AddressBook):
    """
    Adds an email to an existing contact in the address book.

    Prompts the user to enter a name and an email address. If the contact with the given name
    exists in the address book, the email is added to the contact's record. If the contact does
    not exist, an error message is displayed.

    Args:
        book (AddressBook): The address book where the contact is stored.

    Returns:
        None
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name} {Fore.RED}not found.\n")
        return

    email = wrapped_prompt("Enter email: ")
    record.add_email(email)


@input_error(COMMAND_NAMES["add_note"])
def add_note(book: AddressBook):
    """
    Prompts the user to enter a note title and content, then adds the note to the provided AddressBook.

    Args:
        book (AddressBook): The address book to which the note will be added.

    Returns:
        None
    """

    title = wrapped_prompt("Enter note title: ")
    content = wrapped_prompt("Enter note content: ")
    book.add_note(title, content)
    update_notes_completer(book)


@input_error(COMMAND_NAMES["add_phone"])
def add_phone(book: AddressBook):
    """
    Adds a phone number to an existing contact in the address book.
    Prompts the user to enter the name of the contact and the phone number to be added.
    If the contact is found, the phone number is added to the contact's record.
    If the contact is not found, an error message is displayed.
    Args:
        book (AddressBook): The address book containing the contacts.
    Returns:
        None
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name} {Fore.RED}not found.\n")
        return

    phone = wrapped_prompt("Enter phone (10 digits): ")
    record.add_phone(phone)
    print(
        f"\n{Fore.GREEN}Phone {Fore.CYAN}{phone} {Fore.GREEN}added to {Fore.CYAN}{name}{Fore.GREEN}.\n"
    )


@input_error(COMMAND_NAMES["add_tag"])
def add_tag(book: AddressBook):
    """
    Adds a tag to a note in the address book.
    Prompts the user to enter the title of the note and the tag to be added.
    If the note is found, the tag is added to the note and the tags completer is updated.
    If the note is not found, an error message is printed.
    Args:
        book (AddressBook): The address book containing the notes.
    Returns:
        str: A message indicating the result of the operation.
    """

    note_title = wrapped_prompt("Enter note title: ", notes_completer)

    note: Note | None = book.find_note_by_title(note_title)
    if not note:
        return print(f"\n{Fore.RED}Note {Fore.CYAN}{note_title} {Fore.RED}not found.\n")

    tag = wrapped_prompt("Enter tag (#tag): ", completer=tags_completer)
    note.add_tag(tag)
    update_tags_completer(book)


@input_error(COMMAND_NAMES["birthdays"])
def birthdays(book: AddressBook):
    """
    Display upcoming birthdays from the address book.

    This function prompts the user to enter the number of days to look ahead for upcoming birthdays.
    It then retrieves and displays a table of upcoming birthdays within the specified number of days.

    Args:
        book (AddressBook): An instance of AddressBook containing contact information.

    Returns:
        None
    """

    lookup_days = wrapped_prompt("Enter days to lookup: ")
    lookup_days = int(lookup_days)
    upcoming = book.get_upcoming_birthdays(lookup_days)
    upcoming_table = get_birthdays_table(upcoming)
    if len(upcoming) > 0:
        print(f"\n{upcoming_table}\n")
    else:
        print(f"\n{Fore.YELLOW}No upcoming birthdays.\n")


@input_error(COMMAND_NAMES["change_phone"])
def change_phone(book: AddressBook):
    """
    Change the phone number of an existing contact in the address book.

    Prompts the user to enter the name of the contact whose phone number needs to be changed.
    If the contact is found, it then prompts the user to enter the old phone number and the new phone number.
    The old phone number is replaced with the new phone number in the contact's record.

    Args:
        book (AddressBook): The address book containing the contacts.

    Returns:
        None
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)

    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name} {Fore.RED}not found.\n")
        return
    phones_completer = WordCompleter([phone.value for phone in record.phones])
    old_phone = wrapped_prompt("Enter old phone (10 digits): ", phones_completer)
    new_phone = wrapped_prompt("Enter new phone (10 digits): ")
    record.edit_phone(old_phone, new_phone)


@input_error(COMMAND_NAMES["change_address"])
def change_address(book: AddressBook):
    """
    Prompts the user to enter a name and a new address, then updates the address
    of the corresponding contact in the provided AddressBook.

    Args:
        book (AddressBook): The address book containing the contacts.

    Returns:
        None

    Raises:
        None

    Notes:
        If the contact with the specified name is not found in the address book,
        a message will be printed indicating that the contact was not found.
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    address = wrapped_prompt("Enter address: ")
    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name} {Fore.RED}not found.\n")
        return

    record.edit_address(address)


@input_error(COMMAND_NAMES["change_email"])
def change_email(book: AddressBook):
    """
    Change the email address of a contact in the address book.

    Prompts the user to enter the name of the contact and the new email address.
    If the contact is found in the address book, updates the contact's email address.
    If the contact is not found, prints an error message.

    Args:
        book (AddressBook): The address book containing the contacts.

    Returns:
        None
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    email = wrapped_prompt("Enter email: ")
    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name} {Fore.RED}not found.\n")
        return

    record.edit_email(email)


@input_error(COMMAND_NAMES["delete_contact"])
def delete_contact(book: AddressBook):
    """
    Deletes a contact from the given address book.

    Prompts the user to enter the name of the contact to delete and asks for confirmation.
    If the user confirms, the contact is deleted from the address book.

    Args:
        book (AddressBook): The address book from which the contact will be deleted.

    Returns:
        None
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    yes_no_completer = WordCompleter(["yes", "no"])
    result = prompt(
        HTML(f"\nAre you sure you want to delete <cyan>{name}</cyan> (yes/no)?: "),
        completer=yes_no_completer,
    )
    if result.lower() == "yes" or result.lower() == "y":
        book.delete(name)
        update_names_completer(book)


@input_error(COMMAND_NAMES["delete_note"])
def delete_note(book: AddressBook):
    """
    Deletes a note from the given AddressBook by its title.

    Args:
        book (AddressBook): The address book instance from which the note will be deleted.

    Prompts the user to enter the title of the note to be deleted and removes the note with the matching title from the address book.
    """

    title = wrapped_prompt("Enter note title: ", notes_completer)
    book.delete_note_by_title(title)


@input_error(COMMAND_NAMES["edit_note"])
def edit_note(book: AddressBook):
    """
    Edits the content of an existing note in the AddressBook.

    Prompts the user to enter the title of the note they wish to edit and the new content for the note.
    Updates the note in the AddressBook with the new content and prints the updated note.

    Args:
        book (AddressBook): The AddressBook instance containing the notes.

    Returns:
        None
    """

    title = wrapped_prompt("Enter note title: ", notes_completer)
    new_content = wrapped_prompt("Enter new content: ")
    book.edit_note(title, new_content)
    new_note = book.find_note_by_title(title)
    dict_note = {new_note.title: new_note}
    print(f"{Fore.RESET}{get_notes_table(dict_note)}\n")


def find_note_by_title(book: AddressBook):
    """
    Find and display a note by its title from the given address book.

    Args:
        book (AddressBook): The address book instance to search for the note.

    Prompts the user to enter the title of the note they are looking for.
    If the note is found, it prints the note details in a formatted table.
    If the note is not found, it prints a message indicating that the note was not found.
    """

    note_title = wrapped_prompt("Enter note title: ", notes_completer)
    note = book.find_note_by_title(note_title)
    if not note:
        print(f"\n{Fore.RED}Note not found.\n")
    else:
        dict_note = {note.title: note}
        print(f"\n{get_notes_table(dict_note)}\n")


def find_contact_by_name(book: AddressBook):
    """
    Find and display a contact by name from the given address book.

    Args:
        book (AddressBook): The address book to search within.

    Prompts the user to enter a name and searches for the corresponding contact
    in the address book. If the contact is found, it displays the contact's details
    in a formatted table. If the contact is not found, it prints a message indicating
    that the contact was not found.
    """

    name = wrapped_prompt("Enter name: ", names_completer)
    record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact not found.\n")
    else:
        dict_record = {record.name: record}
        print(f"\n{get_contacts_table(dict_record)}\n")


@input_error(COMMAND_NAMES["find_notes"])
def find_notes(book: AddressBook):
    """
    Search for notes in the given AddressBook that match the user's query.

    Args:
        book (AddressBook): The address book containing notes to search.

    Prompts the user to enter a query string and searches for notes in the
    address book that match the query. If no matching notes are found, it
    prints a message indicating that no notes were found. If matching notes
    are found, it prints the notes in a formatted table.

    Returns:
        None
    """

    query = wrapped_prompt("Enter query: ")
    notes = book.find_notes(query)
    if not notes:
        print(f"\n{Fore.RED}No notes found matching {Fore.CYAN}{query}{Fore.RED}.\n")
    else:
        print(f"\n{get_notes_table(notes)}\n")


@input_error(COMMAND_NAMES["find_notes_by_tag"])
def find_notes_by_tag(book: AddressBook):
    """
    Find and display notes associated with a specific tag in the address book.
    Args:
        book (AddressBook): The address book instance containing notes.
    Prompts the user to enter a tag and searches for notes linked to that tag.
    If notes are found, they are displayed in a formatted table. If no notes
    are found, a message indicating the absence of notes linked to the tag is displayed.
    """

    tag = wrapped_prompt("Enter tag (#tag): ", tags_completer)
    notes: list[Note] = book.find_notes_by_tag(tag)
    if not notes:
        print(f"\n{Fore.RED}No notes linked to tag {Fore.CYAN}{tag}{Fore.RED}.\n")
    else:
        print(f"\n{get_notes_table(notes)}\n")


@input_error(COMMAND_NAMES["show_phone"])
def show_phone(book: AddressBook):
    """
    Prompt the user to enter a name, find the corresponding record in the address book,
    retrieve all phone numbers associated with that record, and print them in a table format.

    Args:
        book (AddressBook): The address book to search for the record.

    Returns:
        None
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    record: Record = book.find(name)
    if not record:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name}{Fore.RED} not found.\n")
        return
    phones = record.get_all_phones()
    phones_tale = get_phone_table(phones)
    print(phones_tale)


def get_all_contacts(book: AddressBook):
    """
    Retrieve and display all contacts from the given address book.
    Args:
        book (AddressBook): The address book from which to retrieve contacts.
    Returns:
        None: This function prints the contacts or a message if no contacts are found.
    """

    contacts = book.get_contacts()
    if not contacts:
        print(f"\n{Fore.RED}No contacts found.\n")
    else:
        print(f"\n{get_contacts_table(contacts)}\n")


@input_error(COMMAND_NAMES["remove_tag"])
def remove_tag(book: AddressBook):
    """
    Removes a tag from a note in the address book.

    Args:
        book (AddressBook): The address book containing the notes.

    Returns:
        str: A message indicating whether the note was found or not.

    Prompts:
        - Prompts the user to enter the title of the note.
        - Prompts the user to enter the tag to be removed from the note.
    """

    note_title = wrapped_prompt("Enter note title: ", notes_completer)
    note: Note | None = book.find_note_by_title(note_title)
    tags_completer = WordCompleter([tag.value for tag in note.tags])
    tag = wrapped_prompt("Enter tag (#tag): ", tags_completer)
    if not note:
        return "Note not found"
    note.remove_tag(tag)


@input_error(COMMAND_NAMES["show_birthday"])
def show_birthday(book: AddressBook):
    """
    Display the birthday information of a contact from the address book.

    Prompts the user to enter a name, searches for the corresponding record in the
    provided AddressBook, and if found, prints the birthday information in a table format.
    If the contact is not found, an error message is displayed.

    Args:
        book (AddressBook): The address book containing contact records.

    Returns:
        None
    """

    name = wrapped_prompt("Enter name: ", completer=names_completer)
    record: Record = book.find(name)
    if record:
        birthday_table = get_birthday_table(record)
        print(f"\n{birthday_table}\n")
    else:
        print(f"\n{Fore.RED}Contact {Fore.CYAN}{name}{Fore.RED} not found.")


@input_error(COMMAND_NAMES["all_notes"])
def all_notes(book: AddressBook):
    """
    Display the notes from the given AddressBook.

    Args:
        book (AddressBook): An instance of AddressBook containing notes.

    Returns:
        None
    """

    table = book.get_notes()
    print(f"\n{get_notes_table(table)}\n")


def main():
    """
    Main function to run the command-line interface for the contact book application.

    This function initializes the console, loads data, updates completers, and starts a prompt session
    to accept user commands. It handles various commands to manage contacts, addresses, birthdays, emails,
    notes, and tags. The function also handles saving data and exiting the application gracefully.

    Commands:
    - help: Display available commands.
    - close, exit: Save data and exit the application.
    - add: Add a new contact.
    - add_address: Add an address to a contact.
    - add_birthday: Add a birthday to a contact.
    - add_email: Add an email to a contact.
    - add_note: Add a note.
    - add_phone: Add a phone number to a contact.
    - add_tag: Add a tag to a note.
    - all: Display all contacts.
    - birthdays: Display upcoming birthdays.
    - change_phone: Change contact details.
    - change_address: Change a contact's address.
    - change_email: Change a contact's email.
    - delete_contact: Delete a contact.
    - delete_note: Delete a note.
    - edit_note: Edit a note.
    - find_contact_by_name: Find a contact by name.
    - find_note_by_title: Find a note by title.
    - find_notes: Find notes.
    - find_notes_by_tag: Find notes by tag.
    - phone: Get a contact's phone number.
    - remove_tag: Remove a tag from a note.
    - show_birthday: Show a contact's birthday.
    - all_notes: Show all notes.

    Exceptions:
    - KeyboardInterrupt: Save data and exit on keyboard interrupt.
    - EOFError: Save data and exit on end-of-file error.
    """

    try:
        clear_console()
        book = load_data()
        update_notes_completer(book)
        update_names_completer(book)
        update_tags_completer(book)
        print_formatted_text(welcome_message, style=style)
        session = PromptSession()  # session for in memory history
        while True:
            command = session.prompt(
                HTML("<b><ansibrightcyan>Enter a command:</ansibrightcyan></b> "),
                completer=commands_completer,
            )
            if command in COMMAND_NAMES:
                match command:
                    case "help":
                        print(COMMANDS)
                    case "close" | "exit":
                        save_data(book)
                        print("Good bye!")
                        break
                    case "add_contact":
                        add_contact(book)
                    case "add_address":
                        add_address(book)
                    case "add_birthday":
                        add_birthday(book)
                    case "add_email":
                        add_email(book)
                    case "add_note":
                        add_note(book)
                    case "add_phone":
                        add_phone(book)
                    case "add_tag":
                        add_tag(book)
                    case "all_contacts":
                        get_all_contacts(book)
                    case "birthdays":
                        birthdays(book)
                    case "change_phone":
                        change_phone(book)
                    case "change_address":
                        print(change_address(book))
                    case "change_email":
                        change_email(book)
                    case "delete_contact":
                        delete_contact(book)
                    case "delete_note":
                        delete_note(book)
                    case "edit_note":
                        edit_note(book)
                    case "find_contact_by_name":
                        find_contact_by_name(book)
                    case "find_note_by_title":
                        find_note_by_title(book)
                    case "find_notes":
                        find_notes(book)
                    case "find_notes_by_tag":
                        find_notes_by_tag(book)
                    case "show_phone":
                        show_phone(book)
                    case "remove_tag":
                        remove_tag(book)
                    case "show_birthday":
                        show_birthday(book)
                    case "all_notes":
                        all_notes(book)
            else:
                print(
                    f"\n{Fore.RED}Invalid command.\n{Fore.BLUE}To see all commands available type 'help'\n"
                )
    except (KeyboardInterrupt, EOFError):
        save_data(book)
        print("\nGood bye!")
    except Exception:
        save_data(book)


if __name__ == "__main__":
    main()
