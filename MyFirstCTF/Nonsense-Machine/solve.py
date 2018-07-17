#! /usr/bin/python
# -*- coding: utf-8 -*-
# By : howpwn
# Email : finn79426@gmail.com

from pwn import *

HOST = '140.110.112.30'
PORT = 4119

r = remote(HOST, PORT)

trash = "nonsensenonsense"
REAL_FLAG = ""

r.recvuntil('Here is your flag : ')
flag = b64d(r.recvuntil('\n')[:-1])


print "Please Wait..."


# Part1
r.recvuntil('You also need to tell me some nonsense\n')
while 1:
    enc_trash = b64d(r.recvline()[:-1])
    tmp = xor(enc_trash, trash, flag[:16])
    if 'MyFirstCTF' in tmp:
        REAL_FLAG += tmp
        break
    r.sendlineafter('your turn :', "a")



# Part2
r.sendlineafter('your turn :', "a")
while 1:
    enc_trash = b64d(r.recvline()[:-1])
    tmp = xor(enc_trash, trash, flag[16:])
    if '}' in tmp:
        print tmp
        chk = raw_input("Is this part2 you want?(y/N)")
        if chk == "y\n":
            REAL_FLAG += tmp
            break
    r.sendlineafter('your turn :', "a")



r.close()
print REAL_FLAG

