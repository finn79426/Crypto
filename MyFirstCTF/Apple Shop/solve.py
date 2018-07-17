#! /usr/bin/python
# -*- coding: utf-8 -*-
# By : howpwn
# Email : finn79426@gmail.com

from Crypto.Util.number import *
from hashpumpy import hashpump
from pwn import *

host = "140.110.112.30"
port = 4118
r = remote(host, port)

salt_len = 20
data = "8X3kU8nKpP"

# Get compon
r.readline()
r.readline()
compon = r.readline().split(" ")[5]

b64dcompon = b64d(compon)

# old_hash = sha256(salt + 100compon)
old_hash = b64dcompon[:32] # rdata
# msg = 100compon
msg = b64dcompon[32:] # string

# rdata to hex
old_hash = hex(bytes_to_long(old_hash))[2:] # 0x開頭拿掉，取單純16進制

# 偽造 Hash
new_hash, append_data = hashpump(old_hash, msg, data, salt_len)
new_compon = b64e(long_to_bytes(int(new_hash, 16)) + append_data)

# send new_compon
r.recvuntil("> ")
r.sendline("1")
r.recvuntil("coupon : ")
r.sendline(new_compon)
r.recvuntil("> ")
r.sendline("4")
flag = r.readline()
r.close()
print flag

