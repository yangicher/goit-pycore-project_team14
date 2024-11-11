import pickle
from constants.constants import FILE_NAME
from models.address_book import AddressBook


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
    