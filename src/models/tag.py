from models import Field
import re

tag_regexp = re.compile(r'#?[A-Za-z0-9_]+')

def auto_add_hashtag(tag: str) -> str:
    if not tag.startswith('#'):
        return f'#{tag}'
    return tag

def validate_tag(tag: str) -> None:
    if not re.match(tag_regexp, tag):
        raise TagValidationError()


class Tag(Field):
    def __init__(self, tag: str):
        validate_tag(tag)
        super().__init__(auto_add_hashtag(tag))

class TagValidationError(Exception):
    pass

class TagDuplicateError(Exception):
    pass

class TagNotFound(Exception):
    pass