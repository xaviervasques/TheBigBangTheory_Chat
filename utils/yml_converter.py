#!/usr/bin/python

import json

lines = []
replacements = {'"':'',"'":"","*":"",":":"","[":"","]":"","{":"","`":"","|":"","&":""}

with open('../corpus_data/train_to.txt') as infile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        lines.append(line)
with open('../corpus_data/train_to.txt', 'w') as outfile:
    for line in lines:
        outfile.write(line)

with open('../corpus_data/train_to.txt') as f:
    lines = f.read().splitlines()
    count = 1
    line_split = 1000
    fwrite = open("filename%s.yml" % (count), 'w')
    fwrite.write("categories:\n")
    fwrite.write("- Cornwell\n")
    fwrite.write("conversations:\n")
    for i in xrange(len(lines)):
        line1 = i * 2
        line2 = (i * 2) + 1
        if line1 != len(lines) - 1:
            if line1 == line_split:
                fwrite.write('- - %s\n'%(lines[line1]))
                fwrite.write('  - %s\n'%(lines[line2]))
                fwrite.close()
                count = count + 1
                fwrite = open("filename%s.yml" % (count), 'w')
                fwrite.write("categories:\n")
                fwrite.write("- Cornwell\n")
                fwrite.write("conversations:\n")
                line_split = line_split + 1000
            else:
                fwrite.write('- - %s\n'%(lines[line1]))
                fwrite.write('  - %s\n'%(lines[line2]))
