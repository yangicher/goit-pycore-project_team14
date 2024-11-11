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

- `hello`: Greet the assistant.
- `add_contact <name> <phone>`: Add a new contact.
- `change_phone <name> <old_phone> <new_phone>`: Change the phone number of a contact.
- `show_phone <name>`: Get the phone number of a contact.
- `all_contacts`: List all contacts.
- `add_birthday <name> <birthday>`: Add a birthday to a contact.
- `show_birthday <name>`: Show the birthday of a contact.
- `birthdays <days_lookup>`: Show all birthdays from today to the specified number of days.
- `add_email <name> <email>`: Add an email to a contact.
- `change_email <name> <email>`: Change the email of a contact.
- `add_address <name> <address>`: Add an address to a contact.
- `change_address <name> <address>`: Change the address of a contact.
- `add_phone <name> <phone>`: Add a phone to a contact.
- `add_note <title> <content>`: Add a new note.
- `edit_note <title> <new_content>`: Edit an existing note.
- `delete_note <title>`: Delete a note by title.
- `find_note_by_title <title>`: Find a note by its title.
- `find_notes <query>`: Search notes by title or content.
- `find_notes_by_tag <tag>`: Search notes by tag.
- `add_tag <note_title> <tag>`: Add a tag to a note.
- `remove_tag <note_title> <tag>`: Remove a tag from a note.
- `all_notes`: Show all notes.
- `help`: List available commands.
- `close`/`exit`: Close the assistant.

## Example

```sh
$ python src/main.py
Welcome to the Address Book Assistant!
Type 'help' to see the list of available commands.
Enter a command: add_contact
Enter name: John Doe
Enter phone (10 digits): 1234567890
Contact John Doe added.
Enter a command: show_phone
Enter name: John Doe
Phones of John Doe:
+(123)-456-78-90
Enter a command: add_email
Enter name: John Doe
Enter email: john@example.com
Email john@example.com added to John Doe.
Enter a command: add_address
Enter name: John Doe
Enter address: 123 Main St, Anytown
Address added to John Doe.
Enter a command: add_birthday
Enter name: John Doe
Enter birthday (DD.MM.YYYY): 01.01.1990
Birthday 01.01.1990 added to John Doe.
Enter a command: add_note
Enter note title: Meeting
Enter note content: Discuss project updates
Note Meeting added successfully.
Enter a command: find_note_by_title
Enter note title: Meeting
+---------+----------------------+----------------------+---------------------+
| Title   | Content              | Tags                 | Created             |
+---------+----------------------+----------------------+---------------------+
| Meeting | Discuss project ...  |                      | 2023-10-10 10:00:00 |
+---------+----------------------+----------------------+---------------------+
Enter a command: exit
Good bye!
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.