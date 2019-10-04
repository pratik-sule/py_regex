'''
Quick code to replace elements of string that match a regex pattern

'''
import os

path = "C://Old Laptop//My Docs//CMS//2020//EDGE//New requirements//ERS//XML"

os.chdir(path)

file_name = "Input.txt"

#open input file

ip = open(file_name, "r")

ip_text = ip.readlines()

#close input file
ip.close()

import re

Addr_regex = re.compile(r'R[0-9]+C[0-9]+\:R[0-9]+C[0-9]+')

print(ip_text[0])

test = Addr_regex.search(ip_text[1])

print(test.group())

#Replace address in the string with new address

op = []

start = 33

for ip_line in ip_text:
    
    new_addr = 'R10C' + str(start) + ':R1000C' + str(start)
    
    op_line = re.sub(Addr_regex, new_addr, ip_line)
    
    op.append(op_line)
    
    start = start + 1
    
#write out the output file

with open('output.txt', 'w+') as f:
    for item in op:
        f.write("%s" % item)