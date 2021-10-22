def stringisalnum(s):
    for i in s:
        if i.isalnum():
            return True
    return False
def stringisal(s):
    for i in s:
        if i.isalpha():
            return True
    return False
def stringisdigit(s):
    for i in s:
        if i.isdigit():
            return True
    return False
def stringislower(s):
    for i in s:
        if i.islower():
            return True
    return False
def stringisupper(s):
    for i in s:
        if i.isupper():
            return True
    return False
if __name__ == '__main__':
    s = input()
print(stringisalnum(s))
print(stringisal(s))
print(stringisdigit(s))
print(stringislower(s))
print(stringisupper(s))