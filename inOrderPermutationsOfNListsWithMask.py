#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 LordDarkHelmet (https://github.com/LordDarkHelmet)
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
import timeit
import math

from contextlib import ExitStack
from itertools import permutations

PY3 = sys.version_info[0] == 3
if not PY3:
    print("This program has only been tested on Python 3.6+, you are using an unknown version of python.")
    sys.exit(0)

def sizeoffile_fmt(filesize_bytes):
    for units in ['Bytes','KB','MB','GB','TB']:
        if abs(filesize_bytes) < 1024.0:
            return "%3.1f %s" % (filesize_bytes, units)
        filesize_bytes /= 1024.0
    return "%.1f %s" % (filesize_bytes, 'PB')

parser = argparse.ArgumentParser(description='generates all permutations of N word lists where wordlist 1 is slot 1, wordlist 2 is slot 2, ...')
parser.add_argument("-f", dest="filename", required=True, help="Destination File (where the combined list is stored)", metavar="FILENAME")
parser.add_argument('wordlists', nargs='+', help='The wordlists you would like to combine')
args = parser.parse_args()

start_time = timeit.default_timer()

print('\nStarting...\n')
print('Combining {} wordlists and masks'.format(len(args.wordlists)))

with ExitStack() as stack:
    all_lists = []
    for fname in args.wordlists:
        if os.path.isfile(fname):
            file = stack.enter_context(open(fname, mode='r', encoding='utf-8'))
            all_lists.append(file.read().splitlines())
        elif fname == "?d":
            all_lists.append(("0","1","2","3","4","5","6","7","8","9"))
        elif fname == "?s":
            all_lists.append(("!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","\\","|","?","\"","<",">",":",";",".","/",","))
        else:
            sys.stderr.write("Error: Bad Input!\n")
            sys.exit("Bad Input!")

print('\nNumber of items in each slot:')
all_list_item_count = [ len(listElem) for listElem in all_lists]
print(all_list_item_count)

print('\n')
print('Number of Permutation:')
num_permutations = 1
for x in all_list_item_count:
    num_permutations = num_permutations * x
print("{:,}".format(num_permutations))
print('\nLoading...')

progress_count=0
next_print_percent=0
increment = num_permutations/1000
with open(args.filename, "wb") as file1:
    for line in list(itertools.product(*all_lists)):
        file1.write((''.join(line) + '\n').encode('UTF-8'))
        progress_count += 1
        if next_print_percent <= progress_count:
            next_print_percent = min(progress_count + increment, num_permutations)
            print('Processing... [{:.1f}%]\r'.format((progress_count/num_permutations)*100), end="")

elapsed = timeit.default_timer() - start_time
print("\nNumber of items in file = {:,}".format(progress_count))
print('Execution Time: {:.4f} seconds \n'.format(elapsed))
print('Word List File: [{}] {}'.format(sizeoffile_fmt(os.stat(args.filename).st_size), args.filename))
print('Done!\n')
