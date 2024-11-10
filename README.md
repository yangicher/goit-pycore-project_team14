# goit-pycore-project_team14

This project is a command-line assistant bot that helps manage contacts, including phone numbers, email addresses, physical addresses, birthdays, and notes. The assistant bot supports various commands to add, change, and retrieve contact information.

## Features

- Add, change, and retrieve contact information (phone numbers, email addresses, physical addresses, birthdays).
- Manage notes.
- List all contacts.
- Display upcoming birthdays.
- Save and load contact data using pickle.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yangicher/goit-pycore-project_team14.git
    cd goit-pycore-project_team14
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the assistant bot:

```sh
python src/main.py
```

The assistant bot supports the following commands:

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
- find-notes-by-tag <tag>: Searching notes by entered tag.
- add-email <name> <email>: Add an email to a contact.
- change-email <name> <email>: Change the email of a contact.
- add-address <name> <address>: Add an address to a contact.
- change-address <name> <address>: Change an address for a contact
- add-phone <name> <phone>: Add a phone to a contact.
- add-tag <note title> <tag>: Add tag to a note.
- remove-tag <note title> <tag>: Removing exiting tag from note.
- help: List available commands.
- close/exit: Close the assistant.

## Example

```sh
$ python src/main.py
Welcome to the assistant bot!
Enter a command: add John 1234567890
Contact John added.
Enter a command: phone John
Phones of John:
1234567890
Enter a command: exit
Good bye!
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.