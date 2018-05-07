#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

#!/usr/bin/python
# -*- coding: utf-8 -*- 


from Crypto.Util import number
import gmpy2
import libnum

# problem
n = 66473473500165594946611690873482355823120606837537154371392262259669981906291
e = 65537

# 拿去 fatordb.com 分解N
p = 800644567978575682363895000391634967
q = 83024947846700869393771322159348359271173

# 將flag.enc 引進來
c = number.bytes_to_long(open('flag.enc','rb').read())


# 開始解

# 先算phi_N
phi_n = (p-1) * (q-1)
# 再算出d
d = gmpy2.invert(e, phi_n)
# 已經有d，算出flag明文
flag_as_number = pow(c,d,n)

# 由於flag是數字狀態，再將flag轉成strings
flag_as_strings = libnum.n2s(flag_as_number)
# 顯示flag
print "Here is your flag:\n"
print flag_as_strings

