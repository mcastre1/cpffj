# Given two strings write a method to decide 
# if one is a permutation of the other

# Case sensitive
def are_permutation(str1, str2):
    return sorted(str1) == sorted(str2)

# Case unsensitive
def are_permutation_cu(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

if __name__ == "__main__":
    print(are_permutation_cu("Hello", "elloh"))