# a self-writing program, like MC Escher's "Drawing Hands"
# Goal: to see what it will make with zero direction

import string
import random
import math
import numpy as np
import pandas as pd
import sklearn
import time

random.seed(42)

# f2 = open("hello_world.txt", "w")
# f2.write("a")

for i in range(1000):
    # print i
    # time.sleep(1)
    f = open("hello_world.txt", "r")
    original_program = f.read()
    # print original_program
    # print len(original_program)
    ok_to_write = 1
    new = original_program[:-1]
    # print new
    for i in range(10):
        new+=(random.choice(string.printable))
    # print new
    # print type(new)
    try:
        exec(new)
    except Exception as e:
        ok_to_write = 0
        # print e

    if ok_to_write == 1:
        print i
        f.close()
        f2 = open("hello_world.txt", "w")
        f2.write(new)
        print 'we wrote a new version!'
        print new
        f2.close()
#
# f = open("hello_world.txt", "r")
# original_program = f.read()
# print original_program
# exec(original_program)
