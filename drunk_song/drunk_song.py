import random


def sing(num_bottle, drink):
    """Print our verses of the bottles song."""
    line_1 = "\n{} {} of {} on the wall!"
    line_2 = "{} {} of {}!"
    line_3 = "Take one down and pass it around"
    line_4 = "{} {} of {} on the wall!"
    line_end = "No more bottle of {} on the wall!\n"

    while num_bottle > 0:
        if num_bottle >= 2:
            print(line_1.format(num_bottle, "bottles", drink))
            print(line_2.format(num_bottle, "bottles", drink))
            print(line_3)
            if num_bottle > 2:
                print(line_4.format(num_bottle - 1, "bottles", drink))
            elif num_bottle == 2:
                print(line_4.format(num_bottle - 1, "bottle", drink))
        elif num_bottle == 1:
            print(line_1.format(num_bottle, "bottle", drink))
            print(line_2.format(num_bottle, "bottle", drink))
            print(line_3)
            print(line_end.format(drink))
        num_bottle -= 1


def check_num_bottle(num_bottle):
    """Validate input for number of bottle."""
    try:
        num_bottle = int(num_bottle)
        if num_bottle > 0 and num_bottle < 100:
            return True
        elif num_bottle > 99:
            print("Error: No more than 99 bottles can be sung.")
        elif num_bottle < 1:
            print("Error: No fewer than 1 bottle can be sung.")
    except ValueError:
        print("Error: Input must be an integer.") 
    return False


def main():
    num_bottle = input("Enter a number: ")
    if check_num_bottle(num_bottle) is True:
        drink = input("Enter name of drink: ")
        sing(int(num_bottle), drink)


if __name__ == "__main__":
    main()