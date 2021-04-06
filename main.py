def hiddenpass(s1,s2):
    for i in s2:
        if i in s1 and i==s1[0]:
            s1 = s1[1:]
        elif i in s1 and i!=s1[0]:
            return "FAIL"
        if len(s1)==0:
            return "PASS"
    return "FAIL"


if __name__ == '__main__':
    print(hiddenpass("ABC", "HAPPYBIRTHDAYCACEY"))
    print(hiddenpass("ABC", "TRAGICBIRTHDAYCACEY"))
    print(hiddenpass("ABC", "HAPPYBIRTHDAY"))
    print(hiddenpass("SECRET", "SOMECHORESARETOUGH"))
    print(hiddenpass("SECRET", "SOMECHEERSARETOUGH"))
