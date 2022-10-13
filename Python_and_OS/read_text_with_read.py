#!/usr/bin/env python3

file = open("spider.txt")

print(file.read())

print("next...")

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

print("done")
