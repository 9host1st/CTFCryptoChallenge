def square_root(a, p):
    #Tonelli–Shanks algorithm
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):

    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

c = 3708354049649318175189820619077599798890688075815858391284996256924308912935262733471980964003143534200740113874286537588889431819703343015872364443921848
e = 16
p = 75000325607193724293694446403116223058337764961074929316352803137087536131383
q = 
69376057129404174647351914434400429820318738947745593069596264646867332546443


