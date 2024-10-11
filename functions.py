from pattern import *
import string

spl_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"


# The password length must be at least 12 or above
def length(password):
    if len(password) >= 12:
        return True
    else:
        print("The password is less than 12 characters.")


# The password must have at least 1 upper case character in it
def is_upper(password):
    if any(char in password for char in string.ascii_uppercase):
        return True
    else:
        print("A password must have an Uppercase character (A ... Z).")


# The password must have at least 1 lower case character in it
def is_lower(password):
    if any(char in password for char in string.ascii_lowercase):
        return True
    else:
        print("A password must have a Lowercase character (a ... z).")


# The password must have a digit in it
def is_num(password):
    if any(num in password for num in string.digits):
        return True
    else:
        print("A password must have a number (0 ... 9).")


# The password must have a special character in it
def is_special(password):
    if any(char in password for char in spl_chars):
        return True
    else:
        print(f"A password must have a special character {spl_chars}.")


# The password must have been verified the pattern checker
def is_pattern(password):
    if has_repeating_pattern(password) and has_sequenced_chars(password) and has_consecutive_characters(password):
        return False
    else:
        return True

