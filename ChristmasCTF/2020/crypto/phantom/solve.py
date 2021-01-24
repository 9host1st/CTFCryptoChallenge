import base64
from Crypto.Cipher import Blowfish

ciphertext = base64.b64decode("J8LFHyoEuoo=")

for i in range(256):
    for j in range(256):
        for k in range(256):
            for l in range(256):
                K1 = b"\x9e\x91\x9b\xb3\x3a\xef" + bytes(chr(i) + chr(j), "utf-8")
                K2 = bytes(chr(k) + chr(l), "utf-8") + b"\xf6\xea\x6d\x93\x7f\x22"
                C1 = Blowfish.new(K1, Blowfish.MODE_ECB)
                C2 = Blowfish.new(K2, Blowfish.MODE_ECB)
                D2 = C1.decrypt(ciphertext)
                D1 = C2.decrypt(D2)
                plaintext = base64.b64encode(D1)
                if(b"QUJDREVGR0g=" == plaintext):
                    print(K1)
                    print(K2)
