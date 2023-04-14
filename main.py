from password_generator.password_gen import generate_words, get_word_list, generate_password_based_on_words, get_user_input_words, get_user_input_digits
import random

if __name__ == "__main__":
    gen_word_array = generate_words(get_user_input_words())
    if gen_word_array:
        words_list = get_word_list(gen_word_array)
        password = generate_password_based_on_words(words_list, get_user_input_digits())
        print(password)
    else:
        print("Password generation failed. ")
