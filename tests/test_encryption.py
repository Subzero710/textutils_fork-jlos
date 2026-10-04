from textutils import decrypt, decrypt_without_key, encrypt


def test_encrypt():
    assert encrypt("abc", 3) == "def"


def test_decrypt_with_key():
    assert decrypt("def", 3) == "abc"


def test_decrypt_without_key():
    results = decrypt_without_key("Khoor Zruog")

    assert results[3] == "Hello World"


def test_decrypt_without_key_tests_all_keys():
    results = decrypt_without_key("abc")

    assert len(results) == 26
    assert set(results.keys()) == set(range(26))


def test_encrypt_then_decrypt():
    text = "Open Source 123!"
    encrypted = encrypt(text, 5)

    assert decrypt(encrypted, 5) == text