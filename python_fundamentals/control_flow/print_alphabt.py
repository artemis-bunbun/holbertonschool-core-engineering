#!/usr/bin/env python3

alphabt = ""
print("")
for i in range(ord('a'), ord('z') + 1):
    letter = chr(i)
    if letter not in ['e', 'q']:
        alphabt += letter
print("{}".format(alphabt), end="")
