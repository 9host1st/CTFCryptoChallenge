from pwn import *
from gmpy import gcd, invert

r = remote("lcg.wanictf.org", 50001)
s = []

def gcdList(list):
    return reduce(gcd, list)

def getNext():
    r.recvuntil("> ")
    r.sendline("1")
    x = int(r.recvline())
    return x

def getModular(s):
    ts = []
    us = []
    for i in range(len(s) - 1):
        ts.append(s[i + 1]- s[i])
    for i in range(len(ts) - 2):
        u = abs(ts[i + 2]*ts[i] - ts[i + 1]**2)
        us.append(u)
    return gcdList(us)

def getA(s, m):
    s1 = s[-3]
    s2 = s[-2]
    s3 = s[-1]

    return (s3 - s2) * invert(s2 - s1, m) % m


def getC(s2, a, s1, m):
    return (s2 - (a*s1)) % m

def guess():
    r.sendlineafter("> ", "2")
    print r.recv(2048)
    ans = s[9]
    for i in range(0, 10):
        ans = (a * ans + c) % m
        print(ans)
        r.sendline(str(ans))
        print(r.recv(2048))

for i in range(0, 10):
    s.append(getNext())

m = getModular(s)
a = getA(s, m)
c = getC(s[-1], a, s[-2], m)

r.info("m : " + str(m))
r.info("a : " + str(a))
r.info("c : " + str(c))

assert((a*s[0] + c) % m == (s[1] % m))
guess()
