from functions import *
import argparse
import pyfiglet

# """
# This tool evaluates the password strength based on length, complexity, and entropy.
# """
ascii_banner = pyfiglet.figlet_format("Fortivo")
print(ascii_banner)
print("=========================")
#print("-------------------------")

def password_check(password):
    # Return False if any of the password checks fail, True otherwise
    if not length(password):
        print("Password is too short, it must be atleast 12 characters.")
        return False

    if not is_upper(password):
        print("Password must include at least one uppercase letter.")
        return False

    if not is_lower(password):
        print("Password must include at least one lowercase letter.")
        return False

    if not is_num(password):
        print("Password must include at least one number.")
        return False

    if not is_special(password):
        print("Password must include at least one special character.")
        return False

    if is_pattern(password):
        print("Password contains common patterns or dictionary words.")
        return False

    print(f"You have made a strong password: {password}")
    return True
print("=========================")


def main():
    parser = argparse.ArgumentParser(prog='fortivo',
                                     description='This tool evaluates the password strength based on length, '
                                                 'complexity, and entropy.',
                                     epilog='Remember to follow me at https://github.com/zE0nyx')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('password', type=str, help='Password to evaluate')

    
    args = parser.parse_args()
    password_check(args.password)


if __name__ == '__main__':
    main()
