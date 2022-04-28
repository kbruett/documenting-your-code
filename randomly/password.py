import random
import string
from typing import Optional, Iterable


def generate_password(chars: int, punctuation: bool, invalid_chars: Optional[Iterable[str]]=None) -> str:
    """Create a password from random characters

        Args:
            chars (int): Length of password
            punctuation (bool): Whether to add punctuation to the valid characters
            invalid_chars (Optional[Iterable[str]]): list of characters that are not allowed

        Returns:
            password (str)
    """
    # Add all numbers and letters to the valid characters
    valid_chars = string.ascii_letters + string.digits

    if punctuation:
        # Add punctuation in valid characters
        valid_chars += string.punctuation

    for invalid_char in invalid_chars:
        # Remove argument-entered invalid characters from valid characters
        valid_chars = valid_chars.replace(invalid_char, "")

    # Generate random valid characters and join into password
    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password
