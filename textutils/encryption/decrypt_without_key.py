from .decrypt import decrypt


def decrypt_without_key(text):
    """Generate every possible Caesar decryption without knowing the key.

    The Caesar cipher has only 26 possible shifts, so every possible key
    can be tested.

    Args:
        text (str): The encrypted text.

    Returns:
        dict[int, str]: A mapping containing each possible key and its
        corresponding decrypted text.
    """
    results = {}

    for key in range(26):
        results[key] = decrypt(text, key)

    return results