from colorama import Fore
from models.name import Name
from models.phone import Phone
from models.birthday import Birthday
from models.address import Address
from models.email import Email


class Record:
    """
    A class to represent a contact record.
    Attributes:
    -----------
    name : Name
        The name of the contact.
    phones : list
        A list of Phone objects associated with the contact.
    birthday : Birthday, optional
        The birthday of the contact.
    Methods:
    --------
    __str__():
        Returns a string representation of the contact record.
    add_phone(phone_number: Phone):
        Adds a phone number to the contact's list of phones.
    edit_phone(current_phone, new_phone):
        Edits an existing phone number in the contact's list of phones.
    find_phone(phone_number):
        Finds and returns a phone number from the contact's list of phones.
    get_all_phones():
        Returns all phone numbers associated with the contact.
    add_birthday(birthday):
        Adds a birthday to the contact.
    show_birthdays():
        Returns the birthday of the contact.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}, email: {self.email}, address: {self.address}"

    def add_phone(self, phone_number: Phone):
        """
        Adds a phone number to the record.

        Args:
            phone_number (Phone): The phone number to be added.

        Returns:
            None
        """
        phone = Phone(phone_number)
        if phone:
            self.phones.append(phone)

    def add_email(self, value):
        """
        Adds an email to the record.
        Args:
            value (str): The email address to be added.
        """
        self.email = Email(value)
        print(f"\n{Fore.GREEN}Email {Fore.CYAN}{value} {Fore.GREEN}added to {Fore.CYAN}{self.name}{Fore.GREEN}.\n")

    def add_address(self, address):
        """
        Adds an address to the record.

        Args:
            address (str): The physical address to be added.
        """
        self.address = Address(address)
        print(f"\n{Fore.GREEN}Address added to {Fore.CYAN}{self.name}.\n")

    def edit_email(self, new_email):
        """
        Edits the email address in the record.

        Args:
            new_email (str): The new email address.
        """

        self.email = Email(new_email)
        print(f"\n{Fore.GREEN}Email changed to {Fore.CYAN}{new_email}{Fore.GREEN}.\n")

    def edit_address(self, new_address):
        """
        Edits the address in the record.

        Args:
            new_address (str): The new physical address.
        """
        self.address = Address(new_address)
        print(
            f"\n{Fore.GREEN}Address changed to {Fore.CYAN}{new_address}{Fore.GREEN}.\n"
        )

    def edit_phone(self, current_phone, new_phone):
        """
        Edits an existing phone number in the record.

        Args:
            current_phone (str): The current phone number to be replaced.
            new_phone (str): The new phone number to replace the current one.

        Returns:
            None
        """
        for phone in self.phones:
            if phone.value == current_phone:
                phone.value = new_phone
                print(
                    f"\n{Fore.GREEN}Phone number {Fore.CYAN}{current_phone} {Fore.GREEN}changed to {Fore.CYAN}{new_phone}{Fore.GREEN}.\n"
                )
                break

    def find_phone(self, phone_number):
        """
        Search for a phone number in the list of phone objects.

        Args:
            phone_number (str): The phone number to search for.

        Returns:
            Phone: The phone object if found, otherwise None.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def get_all_phones(self):
        """
        Retrieve all phone numbers associated with the record.

        Returns:
            list: A list of phone numbers.
        """
        return self.phones

    def add_birthday(self, birthday):
        """
        Adds a birthday to the record.

        Args:
            birthday (str): The birthday date in a string format.

        Returns:
            None
        """
        self.birthday = Birthday(birthday)

    def show_birthdays(self):
        """
        Returns the birthday attribute of the record.

        Returns:
            datetime: The birthday of the record.
        """
        return self.birthday

    def change_address(self, new_address: str) -> None:
        """
        Change exiting address to the record.

        Args:
            new_address (str): The home address in the string format.
        """
        self.address = Address(new_address)
