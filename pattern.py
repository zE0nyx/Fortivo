import re


# Check if the password contains a repeating pattern like "abcabcabc123"
def has_repeating_pattern(password):
    match = re.search(r"(..+?)\1", password)
    if match:
        print("A password must not contain repeating pattern.")
    return False


# Check if the password contains consecutive characters like "aaabbbccc111"
def has_consecutive_characters(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            print("A password must not contain consecutive repeating characters.")
        return False


# Check if the password contains sequenced characters like "abcdef12345"
def has_sequenced_chars(password):
    for i in range(len(password) - 2):
        if ((ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2) or
                ord(password[i]) == ord(password[i + 1]) + 1 == ord(password[i + 2]) + 2):
            print("A password must not contain sequenced characters and numbers.")
        return False
