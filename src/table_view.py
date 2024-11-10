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
    table.field_names = ["Name", "Phones", "Birthday", "Email", "Address"]

    for record in contacts.values():
        phones = '; '.join(p.value for p in record.phones) if record.phones else ''
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
    table.field_names = ["Title", "Content", "Tags", "Created At"]

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