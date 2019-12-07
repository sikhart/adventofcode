import sys
import os

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

lines = [line.rstrip('\n') for line in open(file_name)]

objects = {}

for line in lines:
    (val, key) = line.split(')')
    objects[key] = val

count = 0
for obj in objects:
    while obj in objects:
        count += 1
        obj = objects[obj]

print("Part 1: {}".format(count))

you = set()
obj = "YOU"
while obj in objects:
    you.add(obj)
    obj = objects[obj]

san = set()
obj = "SAN"
while obj in objects:
    san.add(obj)
    obj = objects[obj]

print("Part 2: {}".format(len(you.difference(san))+len(san.difference(you))-2))