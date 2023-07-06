from pwn import *

io = process('./binex_1')

payload = "Th1s_is_mY_P@55w0rd"

io.sendline(payload)
io.interactive()