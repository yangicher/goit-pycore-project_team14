import pickle

from colorama import Fore, Style

from models import AddressBook, Record

COMMANDS = """
    Available commands:
    - hello: Greet the assistant.
    - add <name> <phone>: Add a new contact.
    - change <name> <old_phone> <new_phone>: Change the phone number of a contact.
    - phone <name>: Get the phone number of a contact.
    - all: List all contacts.
    - add-birthday <name> <birthday>: Add a birthday to a contact.
    - show-birthday: <name> : Show the birthday of a contact.
    - birthdays: <days_lookup> Show all birthdays from today to days_lookup.
    - add-note <title> <content>: Add a new note.
    - show-notes: Show all notes.
    - delete-note <title>: Delete a note by title.
    - edit-note <title> <new_content>: Edit an existing note.
    - find-notes <query>: Search notes by title or content.
    - add-email <name> <email>: Add an email to a contact.
    - change-email <name> <email>: Change the email of a contact.
    - add-address <name> <address>: Add an address to a contact.
    - change-address <name> <address>: Change an address for a contact
    - help: List available commands.
    - close/exit: Close the assistant.
    """

COMMAND_NAMES = {
    "add": "add",
    "change": "change",
    "phone": "phone",
    "all": "all",
    "help": "help",
    "hello": "hello",
    "close": "close",
    "exit": "exit",
    "add-birthday": "add-birthday",
    "show-birthday": "show-birthday",
    "birthdays": "birthdays",
    "add-email": "add-email",
    "change-email": "change-email",
    "add-address": "add-address",
    "change-address": "change-address",
    "add-note": "add-note",
    "show-notes": "show-notes",
    "delete-note": "delete-note",
    "edit-note": "edit-note",
    "find-notes": "find-notes"
}

FILE_NAME = "address_book.pkl"


def save_data(book, filename=FILE_NAME):
    """
    Save the given book data to a file using pickle.

    Args:
        book (object): The book data to be saved.
        filename (str, optional): The name of the file where the data will be saved. Defaults to FILE_NAME.

    Returns:
        None
    """

    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=FILE_NAME):
    """
    Load data from a file using pickle.

    Args:
        filename (str): The name of the file to load data from. Defaults to FILE_NAME.

    Returns:
        AddressBook: The loaded data if the file exists, otherwise a new AddressBook instance.

    Raises:
        FileNotFoundError: If the file does not exist.
    """

    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def input_error(command_name):
    """
    A decorator to handle errors for command functions in a phone book application.

    Args:
        command_name (str): The name of the command being decorated.

    Returns:
        function: The decorated function with error handling.

    The decorator catches the following exceptions:
        - ValueError: Raised when the input value is incorrect.
        - IndexError: Raised when there are not enough arguments provided.
        - KeyError: Raised when a contact is not found.

    Error messages are customized based on the command name:
        - "add": Error message for adding a contact with missing name or phone number.
        - "change": Error message for changing a contact with missing name or phone number.
        - "phone": Error message for retrieving a phone number with missing user name.
        - "add-birthday": Error message for adding a birthday with missing user name or birthday.
        - "show-birthday": Error message for showing a birthday with missing user name.
        - "add-address": Error message for adding an address with missing user name or address.
        - "change-address": Error message for changing an address with missing name or address.
        - Default: Error message for invalid input.
    """

    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                match command_name:
                    case "add":
                        print(
                            f"Error in '{command_name}' command: Give me a name and a phone number."
                        )
                    case "change":
                        print(
                            f"Error in '{command_name}' command: Give me a name and a phone number."
                        )
                    case "phone":
                        print(f"Error in '{command_name}' command: Enter user name.")
                    case "add-birthday":
                        print(
                            f"Error in '{command_name}' command: Enter user name and birthday."
                        )
                    case "show-birthday":
                        print(f"Error in '{command_name}' command: Enter user name.")
                    case "add-address":
                        return f"Error in '{command_name}' command: Enter contact name and address."
                    case "change-address":
                        print(f"Error in '{command_name}' command: Enter contact name and address.")
                    case "birthdays":
                        print(
                            f"Error in '{command_name}' command: Enter user lookup days."
                        )
                    case _:
                        return print(
                            f"Error in '{command_name}' command: Invalid input."
                        )
            except IndexError:

                print(
                    f"Error in '{command_name}' command: Not enough arguments provided."
                )

            except KeyError:
                print(
                    f"Error in '{command_name}' command: Contact {args[0]} not found."
                )

        return inner

    return decorator


def parse_input(user_input):
    """
    Parses the user input into a command and its arguments.

    Args:
        user_input (str): The input string provided by the user.

    Returns:
        tuple: A tuple where the first element is the command (str) and the remaining elements are the arguments (str).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error(COMMAND_NAMES["add"])
def add_contact(args, book: AddressBook):
    """
    Adds a new contact to the address book.

    Args:
        args (tuple): A tuple containing the name and phone number of the contact.
        book (AddressBook): The address book to which the contact will be added.

    Returns:
        None
    """
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)


@input_error(COMMAND_NAMES["change"])
def change_contact(args, book: AddressBook):
    """
    Change the phone number of an existing contact in the address book.

    Args:
        args (tuple): A tuple containing the contact's name, the old phone number, and the new phone number.
        book (AddressBook): The address book instance where the contact is stored.

    Raises:
        ValueError: If the contact is not found in the address book or the old phone number does not match.
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)


@input_error(COMMAND_NAMES["phone"])
def get_phone(args, book: AddressBook):
    """
    Retrieve and print all phone numbers associated with a given name from the address book.

    Args:
        args (list): A list containing the name as the first element.
        book (AddressBook): An instance of AddressBook to search for the name.

    Returns:
        None
    """
    name = args[0]
    record: Record = book.find(name)
    phones = record.get_all_phones()
    print(f"Phones of {name}:")
    print("\n".join(phone.value for phone in phones))


def get_all_contacts(book: AddressBook):
    """
    Print all contacts in the given address book.

    Args:
        book (AddressBook): The address book containing contact records.

    Returns:
        None
    """
    for record in book.data.values():
        print(record)


@input_error(COMMAND_NAMES["add-birthday"])
def add_birthday(args, book: AddressBook):
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
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        print(f"Birthday {birthday} added to {name}.")
    else:
        print(f"Contact {name} not found.")


@input_error(COMMAND_NAMES["show-birthday"])
def show_birthday(args, book: AddressBook):
    """
    Display the birthday of a contact from the address book.

    Args:
        args (list): A list containing the name of the contact as the first element.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        None: This function prints the birthday of the contact if found,
              otherwise it prints a message indicating the contact was not found.
    """
    name = args[0]
    record = book.find(name)
    if record:
        birthday = record.show_birthdays()
        print(f"{name}'s birthday: {birthday}")
    else:
        print(f"Contact {name} not found.")


@input_error(COMMAND_NAMES["birthdays"])
def birthdays(args, book: AddressBook):
    """
    Prints the upcoming birthdays from the given AddressBook.

    Args:
        book (AddressBook): An instance of AddressBook containing contact information.

    The function retrieves the upcoming birthdays from the AddressBook instance and prints them.
    If there are no upcoming birthdays, it prints a message indicating so.
    """

    lookup_days = int(args[0])

    upcoming = book.get_upcoming_birthdays(lookup_days)
    if len(upcoming) > 0:
        print("Upcoming birthdays:")
        for birthday in upcoming:
            print(f"{birthday['name']}: {birthday['next_upcoming_birthday']}")
    else:
        print("No upcoming birthdays.")

@input_error(COMMAND_NAMES["add-email"])
def add_email(args, book: AddressBook):
    """Add an email to a contact."""
    try:
        name, email = args
        record = book.find(name)
        if record:
            record.add_email(email)
            print(f"Email {email} added to {name}.")
        else:
            print(f"Contact {name} not found.")
    except ValueError as e:
        print(str(e))

@input_error(COMMAND_NAMES["change-email"])
def change_email(args, book: AddressBook):
    """Change the email of a contact."""
    try:
        name, email = args
        record = book.find(name)
        if record:
            record.edit_email(email)
        else:
            print(f"Contact {name} not found.")
    except ValueError as e:
        print(str(e))

@input_error(COMMAND_NAMES["add-address"])
def add_address(args, book: AddressBook):
    """Add an address to a contact."""
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record:
        record.add_address(address)
        print(f"Address added to {name}.")
    else:
        print(f"Contact {name} not found.")

@input_error(COMMAND_NAMES["change-address"])
def change_address(args, book: AddressBook):
    """Change the address of a contact."""
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record:
        record.edit_address(address)
    else:
        print(f"Contact {name} not found.")


@input_error(COMMAND_NAMES['add-address'])
def add_address(args, book: AddressBook) -> str:
    name, address = args
    record: Record | None = book.find(name)
    if not record:
        return f"Contact {name} not found."
    record.add_address(address)
    return f'Address added for {record.name}'


@input_error(COMMAND_NAMES["change-address"])
def change_address(args, book: AddressBook) -> str:
    name, address = args
    record: Record | None = book.find(name)
    if not record:
        return f'Contact {name} not found.'
    elif not record.address:
        return f'There are not addresses for {record.name}'
    record.change_address(address)
    return f'Address for {name} changed.'

@input_error(COMMAND_NAMES["add-note"])
def add_note(args, book: AddressBook):
    """Add a new note to the address book."""
    try:
        title = args[0]
        content = " ".join(args[1:])
        book.add_note(title, content)
    except IndexError:
        print(f"Error: Give me a title and content for the note.")
    except ValueError as e:
        print(str(e))

@input_error(COMMAND_NAMES["show-notes"])
def show_notes(args, book: AddressBook):
    """Show all notes in the address book."""
    book.show_notes()

@input_error(COMMAND_NAMES["delete-note"])
def delete_note(args, book: AddressBook):
    """Delete a note by its title."""
    try:
        title = args[0]
        book.delete_note_by_title(title)
    except IndexError:
        print(f"Error: Give me a title of the note to delete.")
    except ValueError as e:
        print(str(e))

@input_error(COMMAND_NAMES["edit-note"])
def edit_note(args, book: AddressBook):
    """Edit an existing note."""
    try:
        title = args[0]
        new_content = " ".join(args[1:])
        book.edit_note(title, new_content)
    except IndexError:
        print(f"Error: Give me a title and new content for the note.")
    except ValueError as e:
        print(str(e))

@input_error(COMMAND_NAMES["find-notes"])
def find_notes(args, book: AddressBook):
    """Search notes by query."""
    try:
        query = " ".join(args)
        book.find_notes(query)
    except IndexError:
        print(f"Error: Give me a search query.")


def main():
    """
    The main function of the assistant bot. It initializes the AddressBook and
    continuously prompts the user for commands until the user decides to exit.

    Commands:
        - "close" or "exit": Exits the bot.
        - "hello": Greets the user.
        - "add": Adds a new contact to the address book.
        - "change": Changes an existing contact in the address book.
        - "phone": Retrieves the phone number of a contact.
        - "all": Displays all contacts in the address book.
        - "add-birthday": Adds a birthday to a contact.
        - "show-birthday": Shows the birthday of a contact.
        - "birthdays": Lists upcoming birthdays.
        - "add-address": Adds address to a contact.
        - "change-address": Change exiting address to a contact.
        - "help": Displays a list of available commands.

    If an invalid command is entered, an error message is displayed and the user
    is prompted to type 'help' to see all available commands.
    """

    try:
        book = load_data()
        print("Welcome to the assistant bot!")
        while True:
            user_input = input(f"{Style.RESET_ALL}Enter a command: ")
            command, *args = parse_input(user_input)
            if command in COMMAND_NAMES:
                match command:
                    case "close" | "exit":
                        save_data(book)
                        print("Good bye!")
                        break
                    case "hello":
                        print("How can I help you?")
                    case "add":
                        add_contact(args, book)
                    case "change":
                        print(change_contact(args, book))
                    case "phone":
                        print(get_phone(args, book))
                    case "all":
                        get_all_contacts(book)
                    case "add-birthday":
                        add_birthday(args, book)
                    case "show-birthday":
                        show_birthday(args, book)
                    case "birthdays":
                        birthdays(args, book)
                    case "add-email":
                        add_email(args, book)
                    case "change-email":
                        change_email(args, book)
                    case "add-address":
                        print(add_address(args, book))
                    case "change-address":
                        print(change_address(args, book))
                    case "add-note":
                        add_note(args, book)
                    case "show-notes":
                        show_notes(args, book)
                    case "delete-note":
                        delete_note(args, book)
                    case "edit-note":
                        edit_note(args, book)
                    case "find-notes":
                        find_notes(args, book)
                    case "help":
                        print(COMMANDS)
            else:
                print(
                    f"{Fore.RED}Invalid command.\n{Style.RESET_ALL}To see all commands available type 'help'"
                )
    except (KeyboardInterrupt, EOFError):
        save_data(book)
        print("\nGood bye!")


if __name__ == "__main__":
    main()