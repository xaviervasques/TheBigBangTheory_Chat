#!/usr/bin/python
import sys
import json
import math


f1 = open('../corpus_data/valid_from.txt', 'r')
f2 = open('../corpus_data/valid_from_clean.txt', 'w')

for line in f1:
    f2.write(line.replace('"', "'"))
f1.close()
f2.close()

print("{")
print('    "cornwell":')
print("    [")

with open('../corpus_data/valid_from_clean.txt') as f:
    #lines = f.readlines()
    lines = f.read().splitlines()
    for i in range(len(lines)):
        line1 = i * 2
        line2 = (i * 2) + 1
        if line1 < len(lines):
            print("        [")
            print('            "%s",'%(lines[line1]))
            print('            "%s"'%(lines[line2]))
            print("        ],")
        else:
            print("    ]")
            print("}")
            break
