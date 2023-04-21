#暗号文

s = input("英語を入力してください ")


def cipher(s):
    li = []
    result = ""
    for i in range(0, len(s)):
        if s[i].islower():
            li.insert(i, chr(219-ord(s[i])))
        else:
            li.insert(i, s[i])

    for x in range(0, len(s)):
        result += li[x]
    
    return result

print(cipher(s))
