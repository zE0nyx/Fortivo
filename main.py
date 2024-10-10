from functions import *

"""
This tool evaluates the password strength based on length, complexity, and entropy.
"""
print("The password must be at least 12 characters.")
print("The password must include uppercase, lowercase, numbers, and special characters.")
print("No dictionary words, names, easily guessable characters and common patterns.")


def password_check():
    password = input("Enter the password: ")

    if not length(password):
        password_check()
    else:
        if not is_upper(password):
            password_check()
        else:
            if not is_lower(password):
                password_check()
            else:
                if not is_num(password):
                    password_check()
                else:
                    if not is_special(password):
                        password_check()
                    else:
                        if is_pattern(password):
                            password_check()
                        else:
                            print(f"You have made a strong password {password}")


password_check()
