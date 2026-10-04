def encrypt(text, key):
    """Encrypt text using a Caesar cipher.

    Args:
        text (str): The text to encrypt.
        key (int): Number of positions used to shift alphabetic characters.

    Returns:
        str: The encrypted text.
    """
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr((ord(char) - ord("a") + key) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") + key) % 26 + ord("A"))
        else:
            result += char

    return result