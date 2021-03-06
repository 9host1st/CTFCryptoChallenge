from Crypto.Util.number import bytes_to_long

flag = "LAYER7{CENSORED}"

p = random_prime(2^512)
q = random_prime(2^512)

N = p * p * q # 1536bit
e = 0x10001 # 16bit

piN = p * (p-1) * (q-1)

d = inverse_mod(e, piN)
m = bytes_to_long(flag)

ct = pow(m, e, N)

assert pow(ct, d, N) == m

hint = (p * q) % 2^600 # x = pq, hint = x mod 2^600, calculate x.

# f(x) = hint + x*2^600 

print((N, e, ct))
print(hint)
