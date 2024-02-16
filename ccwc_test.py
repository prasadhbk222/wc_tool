import ccwc  # Assuming ccwc.py is in the same directory


def test_count_bytes():
    byte_data = 'こんにちは、世界！'.encode()
    assert ccwc.count_bytes(byte_data) == 27


def test_count_lines():
    byte_data = b'This is a\nsample\nbyte sequence.\n'
    assert ccwc.count_lines(byte_data) == 3


def test_count_words():
    byte_data = b'This is a sample byte sequence.'
    assert ccwc.count_words(byte_data) == 6


def test_count_characters():
    byte_data = 'こんにちは、世界！'.encode()
    assert ccwc.count_characters(byte_data) == 9
