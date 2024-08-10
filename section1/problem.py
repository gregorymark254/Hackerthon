# program that reads a list of integers from the console, removes duplicates sorts the list and print results

def main():
    # Read a list of integers
    numbers = input("Enter a list of numbers(Separate with comma): ")

    # Convert the input string into a list of integers
    try:
        new_numbers = list(map(int, numbers.split(',')))
    except ValueError:
        print("Please enter only integers separated by comma.")
        return

    # Remove duplicates
    unique_numbers = set(new_numbers)

    # Sort the numbers in descending order then print
    sorted_numbers = sorted(unique_numbers, reverse=True)

    print("------SORTED NUMBERS------")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
