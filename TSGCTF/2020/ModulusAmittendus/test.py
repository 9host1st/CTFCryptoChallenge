from Crypto.Util.number import getPrime

p = getPrime(1024)
q = getPrime(1024)

n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

e1 = d % (p - 1)
e2 = d % (q - 1)
cf = pow(q, -1, p)



