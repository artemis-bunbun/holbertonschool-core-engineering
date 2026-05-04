#!/usr/bin/env python3
import os

parent = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
for f in os.listdir(parent):
    print(f)
#x = 1
#if x != 0:
#	print("Language: Python")
#	print("Version: 3")
#	print("Pi approx: 3.14")
#	print("Computation valid: True")
