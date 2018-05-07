#!/usr/bin/python
# -*- coding: utf-8 -*- 

from libnum import n2s # 十進位轉文字
from Crypto.Util import number   # 導入flag
from Crypto.PublicKey import RSA # 導入公鑰
from libnum import solve_crt,nroot
##########################
# 這段程式網路抓就好，google:  Chinese Remainder python

# Chinese Remainder Theorem
def chinese_remainder(n, a):
	sum = 0
	prod = reduce(lambda a, b: a*b, n)
	for n_i, a_i in zip(n, a):
		p = prod / n_i
		sum += a_i * mul_inv(p, n_i) * p
	return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
##########################

# 將檔案load進來
KEY = RSA.importKey(open('public.pem','rb').read())
c = number.bytes_to_long(open('flag.enc','rb').read())

# c = 171593038454590370639160691816701768011631708114057748881162208227300377341431533481821899 
n = KEY.n # 564462951471307835462571845543842769912055276672163683778178867635658249722491250650054821
e = KEY.e # 3

# n 丟factordb.com，得以下
p = 691656593965348479724501935967
q = 736838799725172104070074576411
r = 1107573188787951966821430803233

# c^3 mod p = c mod p = 221211335853089364838057411976 as p1
# c^3 mod q = c mod q = 666763593084936946778597990126 as q1
# c^3 mod r = c mod r = 489130359096392455679033210237 as r1

# 
# "c^3 = p1  (mod p)"
p_root = [111258723643802345601340873881, 183438136792285161537706063165, 396959733529260972585454998921]
q_root = [437268968619046660735525109048]
r_root = [259921130176063805782994055338, 351097072905607274934883479051, 496554985706280886103553268844]

for x in p_root:
    for y in q_root:
        for z in r_root:
            # m = chinese_remainder([p,q,r], [x,y,z])
            m = solve_crt([x,y,z], [p,q,r])
            print n2s(m)

