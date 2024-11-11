from colorama import Fore
from models.tag import TagDuplicateError, TagNotFound, TagValidationError


def input_error(command_name):
    """
    A decorator to handle and display errors for various command functions.

    Args:
        command_name (str): The name of the command to provide specific error messages.

    Returns:
        function: The decorated function with error handling.

    The decorator catches the following exceptions and provides appropriate error messages:
        - TagValidationError: Raised when a tag contains invalid characters.
        - TagDuplicateError: Raised when a duplicate tag is added to a note.
        - TagNotFound: Raised when a specified tag is not found.
        - ValueError: Raised for various value errors, with specific messages based on the command.
        - IndexError: Raised when not enough arguments are provided to a command.
        - KeyError: Raised when a specified contact is not found.
    """

    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TagValidationError:
                return (
                    '\nTag can only include latin chars, numbers and underscore ("_")\n'
                )
            except TagDuplicateError:
                return "\nThis note already include entered tag.\n"
            except TagNotFound:
                return "\nEntered tag not found.\n"
            except ValueError as e:
                if len(e.__str__()):
                    print(f"\n{Fore.RED}Error: '{e}'\n")
                match command_name:
                    case "add_contact" | "change_phone":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Give me a {Fore.CYAN}name{Fore.RED} and a {Fore.CYAN}phone{Fore.RED} number.\n"
                        )
                    case "show_phone" | "delete_contact":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter user {Fore.CYAN}name{Fore.RED}.\n"
                        )
                    case "add_birthday":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter user {Fore.CYAN}name{Fore.RED} and birthday{Fore.RED}.\n"
                        )
                    case "show_birthday":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter user {Fore.CYAN}name{Fore.RED}.\n"
                        )
                    case "add_address" | "change_address":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter contact {Fore.CYAN}name{Fore.RED} and {Fore.CYAN}address{Fore.RED}.\n"
                        )
                    case "birthdays":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter user {Fore.CYAN}lookup days{Fore.RED}.\n"
                        )
                    case "add_phone":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter contact {Fore.CYAN}name{Fore.RED} and {Fore.CYAN}phone{Fore.RED}.\n"
                        )
                    case "add_email":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter contact {Fore.CYAN}name{Fore.RED} and {Fore.CYAN}email{Fore.RED}.\n"
                        )
                    case "change_email":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter contact {Fore.CYAN}name{Fore.RED} and {Fore.CYAN}email{Fore.RED}.\n"
                        )
                    case "add_note":
                        print(f"\n{Fore.RED}Error: '{e}'\n")
                    case "edit_note":
                        print(f"\n{Fore.RED}Error: '{e}'\n")
                    case "delete_note":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter note {Fore.CYAN}title{Fore.RED} to delete\n"
                        )
                    case "find_notes":
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Enter {Fore.CYAN}query{Fore.RED} to search notes\n"
                        )
                    case _:
                        print(
                            f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Invalid input.\n"
                        )
            except IndexError:
                print(
                    f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Not enough arguments provided.\n"
                )
            except KeyError:
                print(
                    f"\n{Fore.RED}Error in {Fore.CYAN}{command_name}{Fore.RED} command: Contact {args[0]} not found.\n"
                )

        return inner

    return decorator