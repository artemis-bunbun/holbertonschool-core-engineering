#!/usr/bin/env python3
import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
#x = 1
#if x != 0:
#	print("Language: Python")
#	print("Version: 3")
#	print("Pi approx: 3.14")
#	print("Computation valid: True")
