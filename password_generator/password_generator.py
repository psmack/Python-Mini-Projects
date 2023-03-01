"""A simple password generator script.

This script takes the following user's password criteria from command line
argument: minimum length, use numbers, and/or use special characters.

Usage examples:

    python3 password_generator.py -ns 20
    python3 password_generator.py -n 20
    python3 password_generator.py -s 20
"""
import argparse
import random
import string
import sys


def get_user_input():
    """
    Use argparse() to parse command line argument for minimum length, number
    flag, and special character flag.

    Returns:
        The arguments int value of minimum length, boolean value for number
        flag, and boolean value for special character flag.
    """
    # Create a parser
    parser = argparse.ArgumentParser(
        prog="password_generator",
        description="Generate password with specified minimum length and \
            optional numbers and special characters",
    )
    # Add int type argument for password minimum length
    min_length = parser.add_argument("length", nargs=1, type=int)
    # Add optional boolean argument for numbers in password
    parser.add_argument(
        "-n", "--number", action="store_true", help="Generate password with numbers"
    )
    # Add optional boolean arugment for special characters in password
    parser.add_argument(
        "-s",
        "--special",
        action="store_true",
        help="Generate password with special characters",
    )

    # args contains parser objects
    args = parser.parse_args()

    return args.length[0], args.number, args.special


def check_min_length(min_length):
    """
    Check if minimum length is between 1 and 40. Program exits if doesn't
    meet criteria.

    Args:
        min_length: An integer value of minimum length for password.
    """
    if min_length < 1 or min_length > 40:
        sys.stderr.write("error: minimum length must be between 1 and 40\n")
        sys.exit(1)


def generate_password(min_length, num=True, special_char=True):
    """
    Generate a string password with alphabets, and numbers and/or special
    characters when specified.

    Args:
        min_length: An integer value of minimum length for password.
        num: If True, generate password with numbers too.
        special_char: If True, generate password with special characters too.

    Returns:
        A generated password string.
    """
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Create a string based on user's specification to use for generating password
    characters = letters
    if num:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # While meets_criteria is False and password's length is less than minimum
    # length, keep adding random character to pwd string.
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        # Update has_number and has_special if the newly random character
        # is a digit or a special character, respectively.
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Update meets_criteria if the password string still doesn't
        # meet the user's criteria.
        meets_criteria = True
        if num:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special

    return pwd


if __name__ == "__main__":
    # Get user input
    min_length, has_number, has_special = get_user_input()
    # Check minimum length value
    check_min_length(min_length)
    # Generate the password
    pwd = generate_password(min_length, has_number, has_special)
    # Show the generated password
    print("Password is:", pwd)
