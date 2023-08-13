# Implement an algorithm to determine if a string has all unique characters

# This implementation is case sensitive. For case unsensitive, we can 
# just turn all characters in string to either upper or lower case.
def is_unique(str):
    # Replace whitespaces in string and then sort all characters.
    sorted_string = sorted(str.replace(" ", "")) 

    # Iterate through characters in string and find repeating ones.
    for i in range(1, len(sorted_string)):
        if sorted_string[i - 1] == sorted_string[i]:
            return False

    return True


if __name__ == "__main__":
    str = "Hi heart"

    print(f"Is the string '{str}' unique? {is_unique(str)}")