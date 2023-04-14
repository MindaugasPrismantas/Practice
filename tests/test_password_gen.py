import string
from unittest.mock import patch
from password_generator.password_gen import generate_words, get_word_list, generate_password_based_on_words, get_user_input_digits, get_user_input_words

words = generate_words(3)
word_list = get_word_list(words)
only_characters = "!?$£&-@#"


def test_generate_words():
    assert all(isinstance(word, str) for word in word_list)


@patch('builtins.input', return_value='')
def test_user_input_word_empty(mock_input):
    result = get_user_input_words()
    assert result == 3


@patch('builtins.input', return_value=5)
def test_user_input_word(mock_input):
    result = get_user_input_words()
    assert result == 5


@patch('builtins.input', return_value='')
def test_user_input_digit_empty(mock_input):
    result = get_user_input_digits()
    assert result == 3


@patch('builtins.input', return_value=5)
def test_user_input_digit(mock_input):
    result = get_user_input_digits()
    assert result == 5


@patch('builtins.input', return_value=5)
def test_user_input_digit_validation(mock_input):
    result = get_user_input_digits()
    assert int(result)


def test_generate_array_length():
    assert len(word_list) == 3


def test_generate_words_min_length():
    for word in word_list:
        assert len(word) >= 4


def test_generate_words_max_length():
    for word in word_list:
        assert len(word) <= 12


def test_generate_password_from_words_capitalised():
    password = generate_password_based_on_words(word_list)
    assert password[0].isupper()


def test_generate_password_from_words_has_digit():
    password = generate_password_based_on_words(word_list)
    assert any(char.isdigit() for char in password)


def test_generate_password_from_words_has_special_char():
    password = generate_password_based_on_words(word_list)
    assert password.find(only_characters)


def test_generate_password_from_words_using_api():
    password = generate_password_based_on_words(word_list)
    assert password.find(string.ascii_letters) & password.find(string.digits) & password.find(string.punctuation) & password[0].isupper()
#     assert password[0].isupper()
#     assert any(char.isdigit() for char in password)
#     assert password.find(only_characters)
#     assert password.find(string.ascii_letters) & password.find(string.digits) & password.find(string.punctuation)

