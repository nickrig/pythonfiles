def rot13(s):
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    trans = chars[26:]+chars[:26]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c) > -1 else c
    return ''.join(rot_char(c) for c in s)
keimeno = raw_input("pliktrologiste to keimeno sas: ")
keim = list(keimeno)
print rot13(keim)