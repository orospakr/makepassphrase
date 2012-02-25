#!/usr/bin/env python

import re
import codecs
import struct
import math

# http://xkcd.com/936/

dict_file = codecs.open("/usr/share/dict/words", "r", "utf8")

words = dict_file.readlines()

noposessives = [x for x in words if not re.search('\'s$', x)]

nolongs = [x for x in noposessives if len(x) < 10]

lowercased = map(unicode.lower, nolongs)

print("There are %i words in the dictionary." % len(lowercased))

wanted_words = 4

bits_per_word = int(math.ceil(math.log(len(lowercased), 2)))

print("Therefore, I'll want %i bits of entropy to select each word." % bits_per_word)

print("Wanted words is %i, therefore need %i bits of entropy." %(wanted_words, bits_per_word * wanted_words))

f = open("/dev/random", "rb")

for i in range(0, wanted_words):
    entropy = f.read(4) # get 32 bits of entropy
    n = struct.unpack("!I", entropy)[0]
    # to get a number between 0 and our length, we're going to use
    # floating point division, which doesn't seem ideal...
    selected = n % len(lowercased)
    print lowercased[selected]
#    print(n *  size_ratio)
    
