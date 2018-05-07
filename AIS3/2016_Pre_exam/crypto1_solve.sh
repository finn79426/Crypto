#!/bin/zsh
#
# crypto1_solve.sh
# Copyright (C) 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.
#

xortool crypto1 -l 39 -o
grep "AIS3" xortool_out -ri --color
rm xortool_out -r

