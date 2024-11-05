from colorama import Fore, Style
import pickle

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
    - birthdays: Show all birthdays.
    - help: List available commands.
    - close/exit: Close the assistant.
    """

COMMAND_NAMES = {
    "add": "add",
    "change": "change",
    "phone": "phone",
    "all": "all",
    "help": "help",
    "close": "close",
    "exit": "exit",
    "add-birthday": "add-birthday",
    "show-birthday": "show-birthday",
    "birthdays": "birthdays",
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
        - Default: Error message for invalid input.
    """

    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                match command_name:
                    case "add":
                        return f"Error in '{command_name}' command: Give me a name and a phone number."
                    case "change":
                        return f"Error in '{command_name}' command: Give me a name and a phone number."
                    case "phone":
                        return f"Error in '{command_name}' command: Enter user nam."
                    case "add-birthday":
                        return f"Error in '{command_name}' command: Enter user name and birthday."
                    case "show-birthday":
                        return f"Error in '{command_name}' command: Enter user name."
                    case _:
                        return f"Error in '{command_name}' command: Invalid input."
            except IndexError:
                return (
                    f"Error in '{command_name}' command: Not enough arguments provided."
                )
            except KeyError:
                return (
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


def birthdays(book: AddressBook):
    """
    Prints the upcoming birthdays from the given AddressBook.

    Args:
        book (AddressBook): An instance of AddressBook containing contact information.

    The function retrieves the upcoming birthdays from the AddressBook instance and prints them.
    If there are no upcoming birthdays, it prints a message indicating so.
    """
    upcoming = book.get_upcoming_birthdays()
    if len(upcoming) > 0:
        print("Upcoming birthdays:")
        for birthday in upcoming:
            print(f"{birthday['name']}: {birthday['next_upcoming_birthday']}")
    else:
        print("No upcoming birthdays.")


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
                        birthdays(book)
                    case "help":
                        print(COMMANDS)
            else:
                print(
                    f"{Fore.RED}Invalid command.\n{Style.RESET_ALL}To see all commands available type 'help'"
                )
    except KeyboardInterrupt:
        save_data(book)
        print("\nGood bye!")


if __name__ == "__main__":
    main()
