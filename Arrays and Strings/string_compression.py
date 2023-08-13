# Implement a method to perform basic string compression
# using the counts of repeated characters.
# If the compressed string would not become smaller than
# the original string, it should return the original string.

def string_compression(str):
    current_char = ''
    count = 0
    compressed_str = ""

    for i in range(len(str)):
        if not str[i] == current_char:
            if not current_char == '':
                compressed_str = f"{compressed_str}{current_char}{count}"

            current_char = str[i]
            count = 1
        else:
            count += 1

    compressed_str = f"{compressed_str}{current_char}{count}"
    
    if len(compressed_str) >= len(str):
        return str
    else:
        return compressed_str

if __name__ == "__main__":
    print(string_compression("aabcccccaaa"))