#! /usr/bin/python
# -*- coding: utf-8 -*-
# By : howpwn
# Email : finn79426@gmail.com

from Crypto.Cipher import DES

m = '89bc8acb348c1ecc'
c = '9e31e5f5a8cef654'
key = ['\x01\x01\x01\x01\x01\x01\x01\x01',
       '\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE',
       '\xE0\xE0\xE0\xE0\xF1\xF1\xF1\xF1',
       '\x1F\x1F\x1F\x1F\x1F\x1F\x1F\x1F',
       ]

for k in key:
    des_func = DES.new(k, DES.MODE_ECB)
    if m == des_func.decrypt(c.decode('hex')).encode('hex'):
        print "SharifCTF{" + k.encode('hex') + "}"
        break
