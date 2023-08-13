# Given a string, write a function to check if its a permutation of a palindrome
# Example: Tact Coa should return True because of Taco Cat palindrome.

def is_palindrome_perm(str):
    str = sorted(str.lower().replace(" ",""))
    char_dict = {str[i]: 0 for i in range(len(str))}

    for c in str:
        char_dict[c] += 1

    odds = 0

    for c in char_dict:
        if not char_dict[c] % 2 == 0:
            odds += 1
        
    if odds > 1:
        return False
    
    return True

if __name__ == "__main__":
    print(is_palindrome_perm("AnIta lava la tina"))