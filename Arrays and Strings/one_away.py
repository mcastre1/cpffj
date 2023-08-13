# Insert, remove, replace. Given two strings write a funtion
# to check if they are one edit away.

def one_way(str1, str2):
    if len(str1) == len(str2):
        return one_replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return one_insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return one_insert(str2, str1)
    return False


def one_replace(str1, str2):
    found_difference = False
    for i in range(len(str1)):
        if not str1[i] == str2[i]:
            if found_difference:
                return False
            else:
                found_difference = True
    
    return True
 
def one_insert(str1, str2):
    index1 = 0
    index2 = 0

    while index2 < len(str2) and index1 < len(str1):
        if not str1[index1] == str2[index2]:
            if not index1 == index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True


if __name__ == "__main__":
    print(one_way("pale", "pal"))
