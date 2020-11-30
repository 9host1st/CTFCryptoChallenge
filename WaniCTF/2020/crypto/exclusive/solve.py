smallEnc = open("output.txt", "r").read()[0:3]
flag = "FLA"
key = ""
def encrypt(s1, s2):
    assert len(s1) == len(s2)

    result = ""
    for c1, c2 in zip(s1, s2):
        result += chr(ord(c1) ^ ord(c2))
    return result

for i in range(0, 3):
    key += chr(ord(smallEnc[i]) ^ ord(flag[i]))


key = key * 19

f = open("output.txt", "r")
enc = (f.read())

print(len(key))
print(len(enc))
print(encrypt(key, enc))
