# Given two strings s1 and s2 write code
# to check if s2 is a rotation of s1.

def is_rotation(s1, s2):
    for i in range(len(s1)):
        s1 = s1[-1] + s1[:-1]
        print(s1)
        if s1 == s2:
            return True
        
    return False

if __name__ == "__main__":
    print(is_rotation("waterbottle", "erbottlewat"))