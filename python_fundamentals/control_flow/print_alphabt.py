#!/usr/bin/env python3
import string

for letter in string.ascii_lowercase:
    if letter not in ['e', 'q']:
        print(letter, end=" ")
