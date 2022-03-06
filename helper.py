
def getNum(s):
    n = ""
    for c in s:
        if c.isdigit():
            n+=c
    return int(n)

def l_sorted(lst):
    return sorted(lst, key=lambda x: getNum(x));
