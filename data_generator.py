#!/usr/bin/env python

import sys, os, re, random, time

try:
    if not os.path.isfile(sys.argv[1]):
        sys.stderr.write("[Error]: %s is not a file\n" % sys.argv[1])
        sys.exit(1)
except IndexError:
    sys.stderr.write("Usage: data_generator.py file\n")
    sys.exit(1)


for count in range(1, 3001):
    time.sleep(random.uniform(1,2))
    file1=open(sys.argv[1],'a+')
    for i in range(1, 4): # ranging from Sensor ID 1 to Sensor ID 3
        temp =str(round(random.uniform(18,30),2))
        humility =str(round(random.uniform(50,80),2))

        file1.write(str(i) +' '+ temp + ' ' + humility +'\n')
        time.sleep(random.uniform(0.0271,0.271))
    file1.close()
    print('count:'+str(count)+' temp:'+ temp + ' humility readings:' + humility +'%')

