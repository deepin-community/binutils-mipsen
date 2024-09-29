#!/usr/bin/env python3

arch_map = {}
host = []
fullc = []
with open("stamp-dir/archmap.tmp") as arcf:
    a=arcf.readline().strip().split(' ')
    for i in a:
        i=i.split('=')
        arch_map[i[0]] = i[1]
    host=arcf.readline().strip().split(' ')

with open("stamp-dir/fullc.tmp") as fullcf:
    fullc = fullcf.readlines()
fullc_len = len(fullc) - 1

for a in arch_map:
    i = fullc.index("Package: binutils-" + arch_map[a] + "\n")
    while i<=fullc_len and fullc[i] != "\n":
        if fullc[i].startswith("Architecture: "):
            print("Architecture: " + " ".join([h for h in host if h != a]))
        else:
            print(fullc[i], end="")
        i += 1
    print()
    i = fullc.index("Package: binutils-" + arch_map[a] + "-dbg\n")
    while i<=fullc_len and fullc[i] != "\n":
        if fullc[i].startswith("Architecture: "):
            print("Architecture: " + " ".join([h for h in host if h != a]))
        else:
            print(fullc[i], end="")
        i += 1
    print()
