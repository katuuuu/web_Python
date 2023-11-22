import re

def check_string(string):
    p = string.count(".")
    a = string.count("@")
    pattern1 = re.compile('^[(+7)8][0-9]{10}$')
    pattern2 = re.compile('^[0-9]{10}$')
    pattern3 = re.compile('^[(+7)8]*[" "]*[\-|\(]*[0-9]{3}[\-|\)]*[" "]*[0-9]{3}[\-]*[0-9]{2}[\-]*[0-9]{2}$')
    pattern4 = re.compile('^[(a-z)]+([(\.)]{1}[a-z]{2,})*[\@]+[a-z]+[\.]{1}[a-z]{2,}([\.]{1}([a-z]{2,}))*$')
    if a == 0:
        if re.match(pattern1, string) or re.match(pattern2, string) or re.match(pattern3, string):
            return True
        else:
            return False
    else:
        if a > 1:
            return False
        elif re.match(pattern4,string):
            return True
        else:
            return False

print(check_string("abc.abc@abc.abc"))