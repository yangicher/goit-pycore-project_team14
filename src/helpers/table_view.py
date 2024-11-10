from prettytable import PrettyTable


def get_contacts_table(contacts):
    """
    Create a formatted table of contacts using PrettyTable.

    Args:
        contacts (dict): Dictionary of contact records

    Returns:
        PrettyTable: Formatted table of contacts
    """
    table = PrettyTable()
    table.field_names = ["Name", "Phone(s)", "Birthday", "Email", "Address"]

    for record in contacts.values():
        phones = '; '.join(p.__str__() for p in record.phones).__str__() if record.phones else ''
        birthday = str(record.birthday) if record.birthday else ''
        email = str(record.email) if record.email else ''
        address = str(record.address) if record.address else ''

        table.add_row([
            record.name.value,
            phones,
            birthday,
            email,
            address
        ])

    table.align = 'l'
    table.max_width = 50
    return table

def get_notes_table(notes):
    """
    Create a formatted table of notes using PrettyTable.

    Args:
        notes (dict): Dictionary of notes

    Returns:
        PrettyTable: Formatted table of notes
    """

    table = PrettyTable()
    table.field_names = ["Title", "Content", "Tags", "Created"]

    for note in notes.values():
        tags = ', '.join(tag.value for tag in note.tags) if note.tags else ''
        created_at = note.creation_date.strftime("%Y-%m-%d %H:%M:%S")

        content = note.value
        if len(content) > 50:
            content = content[:47] + "..."

        table.add_row([
            note.title,
            content,
            tags,
            created_at
        ])

    table.align = 'l'
    table.max_width = 50
    return table

def get_birthdays_table(birthdays):
    """
    Create a formatted table of birthdays using PrettyTable.

    Args:
        birthdays (list): List of upcoming birthdays

    Returns:
        PrettyTable: Formatted table of birthdays
    """
    table = PrettyTable()
    table.field_names = ["Name", "Birthday"]

    for record in birthdays:
        table.add_row([
            record["name"],
            record["next_upcoming_birthday"]
        ])

    table.align = 'l'
    table.max_width = 50
    return table

def get_phone_table(phones):
    """
    Create a formatted table of phones using PrettyTable.

    Args:
        phones (list): List of phone numbers

    Returns:
        PrettyTable: Formatted table of phones
    """
    table = PrettyTable()
    table.field_names = ["Phone(s)"]

    for phone in phones:
        table.add_row([phone])

    table.align = 'l'
    table.max_width = 50
    return table

def get_birthday_table(contact):
    """
    Create a formatted table of birthday using PrettyTable.

    Args:
        contact (Record): Contact record

    Returns:
        PrettyTable: Formatted table of birthday
    """
    table = PrettyTable()
    table.field_names = ["Name", "Birthday"]

    table.add_row([
        contact.name.value,
        contact.birthday
    ])

    table.align = 'l'
    table.max_width = 50
    return table