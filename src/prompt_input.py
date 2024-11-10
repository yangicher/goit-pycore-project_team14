from prompt_toolkit import prompt
from prompt_toolkit.filters import completion_is_selected
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.completion import WordCompleter
from typing import Callable

def prompt_input(commands: list[str]) -> Callable[[str], str]:
    bindings = KeyBindings()

    @bindings.add("enter", filter=completion_is_selected)
    def _(event):
        event.current_buffer.complete_state = None
        event.app.current_buffer.complete_state = None

    def autocomplete_input(message: str):
        return prompt(message, completer=WordCompleter(commands, sentence=True), key_bindings=bindings)

    return autocomplete_input