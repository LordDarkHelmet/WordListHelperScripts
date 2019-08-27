#!/usr/bin/env python3
# Copyright (c) 2019 LordDarkHelmet (https://github.com/LordDarkHelmet)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import os
import sys
import argparse
import itertools

from contextlib import ExitStack
from itertools import permutations


PY3 = sys.version_info[0] == 3
if not PY3:
    print("This program has only been tested on Python 3.6+, you are using an unknown version of python.")
    sys.exit(0)

  
parser = argparse.ArgumentParser(description='generates all permutations in a word list')
parser.add_argument('wordlist', help='The wordlist to generate all permutations', type=argparse.FileType('r'))
parser.add_argument('words', help='The length of the permutations in words', type=int)
args = parser.parse_args()

mylist = args.wordlist.read().splitlines()
args.wordlist.close()

for group in permutations(mylist, args.words):
    print(''.join(group))
