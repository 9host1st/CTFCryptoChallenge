from pwn import *
from gmpy2 import *
from Crypto.Util.number import *

r = remote("185.172.165.118", 4008)
n = (1 << 607) - 1
x = []

def getX():
    r.sendlineafter("> ", "1")
    return int(r.recvline())
for i in range(3):
    x.append(getX())

print(x)
inv  = inverse((x[1] - x[0]), n)
a = ((x[2] - x[1]) * inv) % n
c = (x[1] - a * x[0]) % n
assert a < n
print("[*] a : " + str(a))
print("[*] c : " + str(c))

ans = (a * x[2] + c) % n

r.sendlineafter("> ", "2")
r.sendline(str(ans))

r.interactive()
