#!/usr/bin/env python3

import os

dir = "test_dir"

for object in os.listdir(dir):
    # here, just print out what's inside directory
    print("{} is in the folder".format(object))

    # now, iterate through given directory to test objects
    fullname = os.path.join(dir,object)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

