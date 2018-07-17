#! /usr/bin/python
# -*- coding: utf-8 -*-
# By : howpwn
# Email : finn79426@gmail.com

m1 = "Deposit amount: 5 dollars"
c1 = "5797791557579e322e619f12b0ccdee8802015ee0467c419e7a38bd0a254da54"
m2 = "One million dolls is quite the collection"
c2 = "b1e952572d6b8e00b626be86552376e2d529a1b9cafaeb3ba7533d2699636323e7e433c10a9dcdab2ed4bee54da684ca"
m3 = "Hey nice binoculars"
c3 = "35d0c02036354fdf6082285e0f7bd6d2fdf526bd557b045bce65a3b3e300b55e"

# AES-ECB 介紹：
# 兩個 hex 數字是 1 byte
# 每 16 bytes 是一個 AES-ECB Block, 也就是 32 個 hex 為一個 Block
# 若資料尾未滿 16 bytes, AES-ECB 會幫你 padding 補齊 16 bytes
# 所以任意長度的資料，AES-ECB 出來的 hex 數量一定是 32 的倍數

# 偽造："Deposit amount: " + "One million doll" + "ars"
# len("Deposit amount: ") == 16 # 1 Block
# len("One million doll") == 16 # 1 Block
# len("ars") == 3               # 1 Block (paded)

m = m1[:16] + m2[:16] + m3[16:]
c = c1[:32] + c2[:32] + c3[32:] # it's hex, so length multiply 2
assert len(c) % 32 == 0

print(m)
print(c)
