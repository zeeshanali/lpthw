__author__ = 'hash1'

from sys import argv

program, inputefile = argv

print "read from ", inputefile

in_data=open(inputefile).read()

out_file= raw_input("output file name ?")

print "writing to", out_file

open(out_file,'w').write(in_data)

