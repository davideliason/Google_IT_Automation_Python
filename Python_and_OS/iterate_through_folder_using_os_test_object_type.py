#!/usr/bin/env python3

import os

dir = "test_dir"

for object in os.listdir(dir):
	# here, just print out what's inside directory
	print("{} is in the folder".format(object))

print("done")