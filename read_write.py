#!/usr/bin/python
f=open("test")
while True:
    lines=f.readlines(1000)
    if not lines:
        break
    for line in lines:
        print (line.strip())
f.close()

f=open("test_write","w")
#f=open("test_write","a")
f.write("111111")
f.close()

