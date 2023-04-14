import random
import string
from dotenv import load_dotenv
import http.client
import os
import json

load_dotenv()
api_key = os.environ.get('API_KEY')
host = os.environ.get('API_HOST')


def get_user_input_words():
    while True:
        many_words = input("How many words do you want your password to be: ")
        if many_words == "":
            many_words = 3
            return many_words
        else:
            try:
                many_words = int(many_words)
                return many_words
            except ValueError:
                print("Invalid input. Please enter a valid integer or leave it blank for the default value.")


def get_user_input_digits():
    while True:
        num_digits = input("Enter a number of digits you want to include in the password: ")
        if num_digits == "":
            num_digits = 3
            return num_digits
        else:
            try:
                num_digits = int(num_digits)
                return num_digits
            except ValueError:
                print("Invalid input. Please enter a valid integer or leave it blank for the default value.")


def generate_words(word_amount):
    try:
        connect = http.client.HTTPSConnection(host)
        headers = {
            'X-RapidAPI-Key': api_key,
            'X-RapidAPI-Host': host
        }
        connect.request("GET", f"/getMultipleRandom?count={word_amount}&minLength=6&maxLength=12", headers=headers)
        res = connect.getresponse()
        words = res.read()
        word_array = words.decode('UTF-8')
        return word_array
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_word_list(word_array):
    return json.loads(word_array)


def generate_password_based_on_words(words, num_digits=3):
    special_char = "!?$£&-@#"
    word_list_caps = ''.join([word.capitalize() for word in words])
    word_list = ''.join(word_list_caps)
    digits = ''.join(random.sample(string.digits, num_digits))
    special_character = random.choice([char for char in special_char if char in string.punctuation])
    password = word_list + ''.join(digits) + ''.join(special_character)
    return password


# def get_user_input_char():
#     while True:
#         special_char = input("Enter a special characters to choose from \"!?$£&-@#\": ")
#         if special_char == "":
#             special_char = random.choice("!?$£&-@#")
#             return special_char
#         else:
#             try:
#                 special_char = str(special_char)
#                 return special_char
#             except ValueError:
#                 print("Invalid input. Please enter a valid sign \"!?$£&-@#\" or leave it blank for the default value.")