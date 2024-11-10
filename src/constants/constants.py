from colorama import Fore, Style


COMMANDS = f"""
{Fore.YELLOW}Available commands:{Style.RESET_ALL}
{Fore.GREEN}- help:{Style.RESET_ALL} List available commands.
{Fore.GREEN}- close/exit:{Style.RESET_ALL} Close the assistant.
{Fore.GREEN}- add_address <name> <address>:{Style.RESET_ALL} Add an address to a contact.
{Fore.GREEN}- add_birthday <name> <birthday>:{Style.RESET_ALL} Add a birthday to a contact.
{Fore.GREEN}- add_contact <name> <phone>:{Style.RESET_ALL} Add a new contact.
{Fore.GREEN}- add_email <name> <email>:{Style.RESET_ALL} Add an email to a contact.
{Fore.GREEN}- add_note <title> <content>:{Style.RESET_ALL} Add a new note.
{Fore.GREEN}- add_phone <name> <phone>:{Style.RESET_ALL} Add a phone to a contact.
{Fore.GREEN}- add_tag <note title> <tag>:{Style.RESET_ALL} Add tag to a note.
{Fore.GREEN}- all_contacts:{Style.RESET_ALL} List all contacts.
{Fore.GREEN}- all_notes:{Style.RESET_ALL} Show all notes.
{Fore.GREEN}- birthdays: <days_lookup>{Style.RESET_ALL} Show all birthdays from today to days_lookup.
{Fore.GREEN}- change_phone <name> <old_phone> <new_phone>:{Style.RESET_ALL} Change the phone number of a contact.
{Fore.GREEN}- change_address <name> <address>:{Style.RESET_ALL} Change an address for a contact.
{Fore.GREEN}- change_email <name> <email>:{Style.RESET_ALL} Change the email of a contact.
{Fore.GREEN}- close/exit:{Style.RESET_ALL} Close the assistant.
{Fore.GREEN}- delete_contact <name>:{Style.RESET_ALL} Delete a note by title.
{Fore.GREEN}- delete_note <title>:{Style.RESET_ALL} Delete a note by title.
{Fore.GREEN}- edit_note <title> <new_content>:{Style.RESET_ALL} Edit an existing note.
{Fore.GREEN}- find_contact_by_name <name>:{Style.RESET_ALL} Searching contact by entered name.
{Fore.GREEN}- find_note_by_title <title>:{Style.RESET_ALL} Searching note by entered title.
{Fore.GREEN}- find_notes <query>:{Style.RESET_ALL} Search notes by title or content.
{Fore.GREEN}- find_notes_by_tag <tag>:{Style.RESET_ALL} Searching notes by entered tag.
{Fore.GREEN}- remove_tag <note title> <tag>:{Style.RESET_ALL} Removing exiting tag from note.
{Fore.GREEN}- show_phone <name>:{Style.RESET_ALL} Get the phone number of a contact.
{Fore.GREEN}- show_birthday: <name> :{Style.RESET_ALL} Show the birthday of a contact.
"""

COMMAND_NAMES = {
    "help": "help",
    "close": "close",
    "exit": "exit",
    "add_address": "add_address",
    "add_birthday": "add_birthday",
    "add_contact": "add_contact",
    "add_email": "add_email",
    "add_note": "add_note",
    "add_phone": "add_phone",
    "add_tag": "add_tag",
    "all_contacts": "all_contacts",
    "all_notes": "all_notes",
    "birthdays": "birthdays",
    "change_phone": "change_phone",
    "change_address": "change_address",
    "change_email": "change_email",
    "delete_contact": "delete_contact",
    "delete_note": "delete_note",
    "edit_note": "edit_note",
    "exit": "exit",
    "find_contact_by_name": "find_contact_by_name",
    "find_note_by_title": "find_note_by_title",
    "find_notes": "find_notes",
    "find_notes_by_tag": "find_notes_by_tag",
    "help": "help",
    "remove_tag": "remove_tag",
    "show_phone": "phone",
    "show_birthday": "show_birthday",
}
FILE_NAME = "address_book.pkl"
