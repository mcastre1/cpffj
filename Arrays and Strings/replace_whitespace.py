def replace_whitespace(str, sub):
    str = str.split()
    temp = ""
    for i in range(len(str) - 1):
        temp += str[i] + sub

    temp += str[-1]
    return temp 

if __name__ == "__main__":
    print(replace_whitespace("Mr John Smith   ", "%20"))