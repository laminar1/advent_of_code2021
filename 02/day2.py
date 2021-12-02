#!/usr/bin/env python
#
# day2.py
#
# Created by Scott Lee on 12/1/21.
#
#

'''
Description: 

'''

test_data = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]

with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

print(lines)

real_data = lines

horizontal = 0
depth = 0
aim = 0


for cmd in real_data:
    direction = cmd.split(' ')[0]
    magnitude = int(cmd.split(' ')[1])
    if 'forward' in direction:
        horizontal += magnitude
        depth += aim * magnitude
    if 'down' in direction:
        aim +=  magnitude
    if 'up' in direction:
        aim -= magnitude

score = horizontal * depth

print(f'horizontal: {horizontal}')
print(f'depth: {depth}')
print(f'score: {score}')
