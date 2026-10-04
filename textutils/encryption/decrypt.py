def decrypt(text, key):
    """Decrypt text encrypted with a Caesar cipher.

    Args:
        text (str): The encrypted text.
        key (int): Shift used during encryption.

    Returns:
        str: The decrypted text.
    """
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr((ord(char) - ord("a") - key) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") - key) % 26 + ord("A"))
        else:
            result += char

    return result