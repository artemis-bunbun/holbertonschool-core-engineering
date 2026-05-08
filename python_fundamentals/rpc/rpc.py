#!/usr/bin/env python3

import random

pscore = 0
rscore = 0


ptool = 0
rtool = 0

rock = 1
paper = 2
scissor = 3
print("\n")
name = input("enter your username: ")
print(" ")
print(" ")
print("Username chosen: {}".format(name))

rtool = random.randint(1, 3)
if rtool == 1:
    computer = "Rock"
elif rtool == 2:
    computer = "Paper"
else:
    computer = "Scissors"

if ptool == "1":
	tool = "Rock"
elif ptool == "2":
	tool = "Paper"
else:
	tool = "Scissors"

while pscore < 3 and rscore < 3:
	ptool = input("choose your tool: rock[1], paper[2], scissor[3]")
	if ptool == "1":
		print("{} played: {}".format(name, tool))
		print("Computer chose...")
		print("{}!".format(computer))
		break
if tool == "Rock" and computer == "Scissors":
			print("{} beat the computer and won with {} out of 3".format(name, pscore))

